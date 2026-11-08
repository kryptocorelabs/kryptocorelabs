# KryptoCoreLabs

**One open foundation. A growing ecosystem. Security built together.**

We build privacy-focused software that helps people retain control of their data
and keys. The whole ecosystem is open source: the Core, shared modules, Vault,
Firefox extension, Container, Messenger and Rescue. First-party code is MIT
licensed; third-party components retain their own terms.

## Why KryptoCore?

Established cryptography is the starting point. We focus on a small reusable
Core, clear interfaces, documented formats and tests contributors can reproduce.
Applications own their additional trust boundaries and responsibilities.
Open source enables scrutiny; it does not guarantee security.

Read our [project charter](https://github.com/kryptocorelabs/kryptocore/blob/main/PROJECT_CHARTER.md) for the technical direction, community
principles, funding policy and limits on security claims.

Testing to date has been carried out by the KryptoCoreLabs maintainers, locally
and through automated CI. No independent security audit has been completed.
We welcome community testing, code reviews and scrutiny of our security
assumptions. Please use synthetic data and report suspected vulnerabilities
privately through the project's security-reporting channel.

## Projects

| Project | Implementation | Status and downloads |
| --- | --- | --- |
| Core and optional signatures | [kryptocore](https://github.com/kryptocorelabs/kryptocore) | Rust library and Python interoperability reference; preview |
| Vault and Firefox | [vault-source](https://github.com/kryptocorelabs/vault-source) | [Vault previews](https://github.com/kryptocorelabs/vault); Firefox 0.1.16 is Mozilla-signed |
| Messenger | [apps-source/apps/msg](https://github.com/kryptocorelabs/apps-source/tree/main/apps/msg) | [Experimental Tor chat and files](https://github.com/kryptocorelabs/msg) |
| Container | [apps-source/apps/container](https://github.com/kryptocorelabs/apps-source/tree/main/apps/container) | [Encrypted file archives](https://github.com/kryptocorelabs/container); preview |
| Rescue | [apps-source/apps/rescue](https://github.com/kryptocorelabs/apps-source/tree/main/apps/rescue) | [Offline recovery exports](https://github.com/kryptocorelabs/rescue); MSG recovery not implemented |
| Verify | [apps-source/apps/verify](https://github.com/kryptocorelabs/apps-source/tree/main/apps/verify) | Offline signed-release checks; preview, official release-key provisioning pending |

The application workspaces contain shared modules so they can be cloned, built
and tested independently. The separate app repositories remain their download
and user-documentation entry points.

## Build with us

Developers, reviewers, security researchers and documentation contributors are
welcome. Start with a source repository's README and contribution guide, or
join [Discussions](https://github.com/kryptocorelabs/kryptocore/discussions).
Report vulnerabilities through the private security-reporting channel.

Donations are the primary intended funding source. Optional support, maintenance
agreements or hosted services may help fund ongoing work. Local applications,
their source and access to one's own data stay freely available.

All applications remain previews. Independent security audit is pending;
Windows executables are unsigned. Mozilla signing of the Firefox package is
separate from an audit of Vault or the broader ecosystem.
