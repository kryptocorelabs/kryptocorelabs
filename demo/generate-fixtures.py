"""Build and check the synthetic demo using KryptoCore's native workers."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import tempfile
import time


INPUTS = Path(__file__).resolve().parent / "inputs"
VAULT_PASSWORD = "Northstar demo vault only"
RECOVERY_KEY = "0123456789abcdef" * 4
CONTAINER_PASSWORD = "Northstar demo transfer only"
# RFC 8032 test vector 1. This key is public and is never a publisher key.
TEST_SEED = "9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60"
TEST_PUBLIC = "KCP1:d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a"


def framed(worker, metadata, first="", second="", *, expected=True):
    fields = (json.dumps(metadata).encode(), first.encode(), second.encode())
    request = b"".join(struct.pack("<I", len(field)) + field for field in fields)
    result = subprocess.run([worker], input=request, capture_output=True, check=True, timeout=60)
    reply = json.loads(result.stdout)
    if reply["ok"] != expected:
        raise RuntimeError(f"{metadata['action']}: {reply['message']}")
    return reply


def vault(worker, destination, entries):
    path = str(destination)
    requests = [
        dict(action="open", path=path, create=True, password=VAULT_PASSWORD, recovery=RECOVERY_KEY),
        *(dict(action="put", site=entry["origin"], username=entry["username"],
               password=entry["password"]) for entry in entries),
    ]
    result = subprocess.run(
        [worker, "desktop-session"], input="".join(json.dumps(req) + "\n" for req in requests),
        encoding="utf-8", capture_output=True, check=True, timeout=60,
    )
    replies = [json.loads(line) for line in result.stdout.splitlines()]
    if len(replies) != len(requests) or any("error" in reply for reply in replies):
        raise RuntimeError("Vault could not create the synthetic logins")
    if destination.read_bytes()[:4] != b"KCV2":
        raise RuntimeError("Expected a recovery-enabled KCV2 file")


def verify_fixture(worker, openssl, target, temporary):
    target.mkdir()
    artifact = INPUTS / "files" / "transfer-note.txt"
    payload = artifact.read_bytes()
    now = int(time.time())
    manifest = target / "release.json"
    signature = target / "release.sig"
    manifest.write_bytes(json.dumps({
        "schema": "kryptocore-release/v1",
        "product": "northstar-demo",
        "version": "1.0-demo",
        "sequence": 1,
        "issued_at": now - 3600,
        "expires_at": now + 365 * 86400,
        "source_commit": "0" * 40,
        "artifacts": [{"file": artifact.name, "target": "demo", "length": len(payload),
                       "sha256": hashlib.sha256(payload).hexdigest()}],
    }, separators=(",", ":")).encode())
    purpose = b"release-manifest/v1"
    message = manifest.read_bytes()
    frame = temporary / "frame.bin"
    frame.write_bytes(b"KryptoCore/signatures\x00\x01" + struct.pack(">H", len(purpose))
                      + purpose + struct.pack(">Q", len(message)) + message)
    test_key = temporary / "public-test-seed.der"
    test_key.write_bytes(bytes.fromhex("302e020100300506032b657004220420" + TEST_SEED))
    subprocess.run([openssl, "pkeyutl", "-sign", "-rawin", "-keyform", "DER",
                    "-inkey", test_key, "-in", frame, "-out", signature], check=True, timeout=20)
    (target / "demo-public-key.txt").write_text(TEST_PUBLIC + "\n", encoding="ascii")

    def check(file):
        return subprocess.run([worker, "check", file, manifest, signature,
                               "--key", TEST_PUBLIC, "--product", "northstar-demo",
                               "--version", "1.0-demo", "--target", "demo"],
                              capture_output=True, text=True, timeout=20)

    accepted = check(artifact)
    changed = temporary / artifact.name
    changed.write_bytes(bytes([payload[0] ^ 1]) + payload[1:])
    rejected = check(changed)
    if accepted.returncode != 0 or rejected.returncode != 1:
        raise RuntimeError(f"Verify failed its positive/negative checks: {accepted.stderr} {rejected.stderr}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="a new output directory")
    for worker in ("vault", "container", "rescue", "verify"):
        parser.add_argument(f"--{worker}", type=Path, required=True)
    parser.add_argument("--openssl", default="openssl")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir()
    login_entries = json.loads((INPUTS / "logins.json").read_bytes())["entries"]
    vault_path = output / "demo-vault.kcv"
    container_path = output / "demo-container.kcc"
    vault(args.vault.resolve(), vault_path, login_entries)
    sources = [INPUTS / "files" / name for name in ("packing-list.csv", "transfer-note.txt")]
    engine = args.container.resolve()
    framed(engine, dict(action="pack", output=str(container_path),
                        sources=list(map(str, sources)), opener=None),
           CONTAINER_PASSWORD, CONTAINER_PASSWORD)
    with tempfile.TemporaryDirectory(prefix="kryptocore-demo-check-") as work:
        work = Path(work).resolve()
        before = vault_path.read_bytes()
        for route, secret in (("password", VAULT_PASSWORD), ("recovery_key", RECOVERY_KEY),
                              ("password", "deliberately wrong password")):
            destination = work / (route + ".json")
            expected = secret != "deliberately wrong password"
            framed(args.rescue.resolve(), dict(action="recover", input=str(vault_path),
                   output=str(destination), credential=route, confirm_plaintext=True),
                   secret, expected=expected)
            if expected:
                if json.loads(destination.read_bytes()) != login_entries:
                    raise RuntimeError("Rescue exported different entries")
                destination.unlink()
            elif destination.exists():
                raise RuntimeError("Rescue created output with a wrong password")
        if vault_path.read_bytes() != before:
            raise RuntimeError("Rescue modified the original vault")
        destination = work / "unpacked"
        framed(engine, dict(action="unpack", input=str(container_path), output=str(destination)),
               CONTAINER_PASSWORD)
        for source in sources:
            if (destination / source.name).read_bytes() != source.read_bytes():
                raise RuntimeError("Container unpacked different bytes")
        verify_fixture(args.verify.resolve(), args.openssl, output / "verify", work)
    print("Vault, both Rescue credential routes, Container and Verify passed with synthetic data.")


if __name__ == "__main__":
    main()
