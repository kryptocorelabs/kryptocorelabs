# KryptoCoreLabs

## KryptoCore Vault

**An open-source password manager for people who want to keep their logins on their own device.**

Vault saves your logins in an encrypted file you can open offline. No account
or cloud service is required.

**Windows preview.** Try it with sample data.

[Try the Windows preview](https://github.com/kryptocorelabs/vault#try-the-desktop-preview) · [Browse the source](https://github.com/kryptocorelabs/vault-source) · [Give feedback](https://github.com/kryptocorelabs/vault/issues)

[See Vault with sample logins](demo/README.md#vault).

## Projects

Vault is built on KryptoCore, a reusable encryption library. The other projects
are available separately for people who want to explore or contribute.

| Project | Implementation | Status and downloads |
| --- | --- | --- |
| Firefox companion | [vault-source](https://github.com/kryptocorelabs/vault-source) | [Mozilla-signed add-on for compatible Windows Vault builds](https://github.com/kryptocorelabs/vault/blob/main/FIREFOX.md) |
| Container | [apps-source/apps/container](https://github.com/kryptocorelabs/apps-source/tree/main/apps/container) | [Preview for encrypted file archives](https://github.com/kryptocorelabs/container) |
| Rescue | [apps-source/apps/rescue](https://github.com/kryptocorelabs/apps-source/tree/main/apps/rescue) | [Preview for offline Vault and Container recovery exports](https://github.com/kryptocorelabs/rescue) |
| Messenger | [apps-source/apps/msg](https://github.com/kryptocorelabs/apps-source/tree/main/apps/msg) | [Experimental Tor chat and file transfers](https://github.com/kryptocorelabs/msg) |
| Core and optional signatures | [kryptocore](https://github.com/kryptocorelabs/kryptocore) | Rust encryption library and Python interoperability reference, both in preview |
| Verify | [apps-source/apps/verify](https://github.com/kryptocorelabs/apps-source/tree/main/apps/verify) | Preview for offline checks of signed releases using the [published verification key](https://github.com/kryptocorelabs/kryptocore/blob/main/PUBLIC_RELEASE_KEY.txt). |

## Why KryptoCore?

We build local tools so people can control their data and keys. First-party code
is open source under MIT. We use established cryptography, keep the reusable
Core small and document what each app protects. See the [project charter](https://github.com/kryptocorelabs/kryptocore/blob/main/PROJECT_CHARTER.md).

## Build with us

Start with the [demo walkthrough and screenshots](demo/README.md).
Try the apps with public synthetic data, including a filled vault, encrypted
files, a loopback chat and a signed sample for Verify.

Developers, reviewers, security researchers and documentation contributors are
welcome. Start with a source repository's README and contribution guide, or
join [Discussions](https://github.com/kryptocorelabs/kryptocore/discussions).
Report vulnerabilities through the private security-reporting channel.

Donations are the primary intended funding source. Optional support, maintenance
agreements or hosted services may help fund ongoing work. Local applications,
their source and access to one's own data stay freely available.

All apps are previews. Testing to date comes from maintainers and automated CI.
An independent security audit is pending. Windows executables are unsigned.

[Security in 30 seconds](https://github.com/kryptocorelabs/kryptocore/blob/main/SECURITY-IN-BRIEF.md) · [Recovery guide](https://github.com/kryptocorelabs/kryptocore/blob/main/RESCUE-FIRST.md) · [Verify downloads](https://github.com/kryptocorelabs/kryptocore/blob/main/VERIFY-DOWNLOADS.md)
