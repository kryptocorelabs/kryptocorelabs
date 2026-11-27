# KryptoCoreLabs

**One Core. Many Apps. One Community.**

KryptoCoreLabs builds an open-source ecosystem of privacy and security tools
around a shared cryptographic foundation.

Our goal is to make digital privacy accessible to everyone, without mandatory
cloud services, accounts, subscriptions or unnecessary technical complexity.
Local use must not require telemetry. Users retain control over their own
data, keys and choices.

**Development previews.** Testing to date comes from maintainers and automated
CI. No independent security audit has been completed. Try the apps with
synthetic data and retain backups.

[Explore the demos](demo/README.md) · [Build with us](#build-with-us) · [Discuss ideas](https://github.com/kryptocorelabs/kryptocore/discussions)

## Projects

| Project | Purpose and status | Source and downloads |
| --- | --- | --- |
| Core and optional signatures | Small local Rust encryption library, Python interoperability reference and separate signature companion. Preview. | [Source, tests and integration guide](https://github.com/kryptocorelabs/kryptocore) |
| Vault | Local password manager. The current Windows preview ZIP requires Python 3.13 x64 and setup. | [Download and setup](https://github.com/kryptocorelabs/vault#try-the-desktop-preview) · [Source](https://github.com/kryptocorelabs/vault-source) |
| Firefox companion | Mozilla-signed 0.1.16 for Firefox 140+. Pairing requires a compatible Windows Vault build. | [Installation](https://github.com/kryptocorelabs/vault/blob/main/FIREFOX.md) · [Source](https://github.com/kryptocorelabs/vault-source) |
| Container | Encrypted KCC archives and an optional self-extracting Windows EXE. Preview. | [Downloads and guide](https://github.com/kryptocorelabs/container) · [Source](https://github.com/kryptocorelabs/apps-source/tree/main/apps/container) |
| Messenger | Experimental chat and file transfers over Tor. Both participants must be online. | [Windows preview](https://github.com/kryptocorelabs/msg) · [Source](https://github.com/kryptocorelabs/apps-source/tree/main/apps/msg) |
| Rescue | Offline exports from supported Vault and Container files, using existing valid credentials. Preview. | [Windows preview](https://github.com/kryptocorelabs/rescue) · [Source](https://github.com/kryptocorelabs/apps-source/tree/main/apps/rescue) |
| Verify | Offline checks of signed release manifests using an explicitly trusted publisher key. Preview. | [Source and native CI build guide](https://github.com/kryptocorelabs/apps-source/tree/main/apps/verify) · [Published key](https://github.com/kryptocorelabs/kryptocore/blob/main/PUBLIC_RELEASE_KEY.txt) |

## Why KryptoCore?

First-party code is open source under MIT; dependencies retain their own terms.
The Core provides local cryptographic operations. Apps own their formats,
storage, interfaces and networking. Messenger uses Snow for its Noise protocol
and Tor for transport. The Core is not a universal identity or login key.
See the [project charter](https://github.com/kryptocorelabs/kryptocore/blob/main/PROJECT_CHARTER.md)
and [Core security contract](https://github.com/kryptocorelabs/kryptocore/blob/main/CORE_SECURITY_CONTRACT.md).

Security claims must follow documented mechanisms, tests and limitations.
Open source invites scrutiny; it does not guarantee security. A signed release
manifest establishes release provenance against a trusted key, not that a file
is harmless. Windows executables are not Authenticode-signed; publisher
manifest signatures and Mozilla add-on signing are separate checks.

## Build with us

Start with the [demo walkthrough and screenshots](demo/README.md).
Try the apps with public synthetic data, including a filled vault, encrypted
files, a loopback chat and a signed sample for Verify.

Developers, reviewers, security researchers and documentation contributors are
welcome. Follow a source repository's README to build and test, then read its
contribution guide. The [Core contribution guide](https://github.com/kryptocorelabs/kryptocore/blob/main/CONTRIBUTING.md)
and [good first issues](https://github.com/kryptocorelabs/kryptocore/labels/good%20first%20issue)
provide starting points. Reproducible bug reports should use synthetic inputs
and include the app version, platform, steps and expected result.

Discuss ideas in [Discussions](https://github.com/kryptocorelabs/kryptocore/discussions).
Report suspected vulnerabilities privately through the [security policy](https://github.com/kryptocorelabs/kryptocore/blob/main/SECURITY.md).
Key handling, formats, recovery and browser/network boundaries need particular
review. Never attach real vaults, passwords or identities to public reports.

Donations are the primary intended funding source. Optional support, maintenance
agreements or hosted services may help fund ongoing work. Local applications,
their source and access to one's own data stay freely available.

**Your data. Your device. Your choice.**

[Security in 30 seconds](https://github.com/kryptocorelabs/kryptocore/blob/main/SECURITY-IN-BRIEF.md) · [Recovery guide](https://github.com/kryptocorelabs/kryptocore/blob/main/RESCUE-FIRST.md) · [Verify downloads](https://github.com/kryptocorelabs/kryptocore/blob/main/VERIFY-DOWNLOADS.md)
