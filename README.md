# KryptoCoreLabs

We build local encryption tools so people can keep control of their data
and keys. A small, reusable library is the foundation for the apps we
want to build.

## A free core

[KryptoCore](https://github.com/kryptocorelabs/kryptocore) is a Rust library
for authenticated encryption and password-based key derivation. The core
is free to use, inspect, improve, and build on under the MIT license.
We welcome independent applications built on it.

## Apps built on the core

| Project | Status |
| --- | --- |
| [Vault](https://github.com/kryptocorelabs/vault) | Windows password manager. [Public previews](https://github.com/kryptocorelabs/vault/releases) are available for evaluation with synthetic data. |
| [Firefox integration](https://github.com/kryptocorelabs/vault/blob/main/FIREFOX.md) | Release candidate tested with Vault for Windows. Persistent installation depends on a Mozilla-signed build. |
| [MSG](https://github.com/kryptocorelabs/msg) | Windows alpha for encrypted conversations and file transfers over Tor. |
| [Rescue](https://github.com/kryptocorelabs/rescue) | Offline preview: authenticate/export Vault records and extract Container archives to fresh destinations. MSG recovery is not implemented. |
| [Container](https://github.com/kryptocorelabs/container) | Windows alpha for portable encrypted archives and self-opening exports. |

We want donations and optional paid app features to help fund ongoing
maintenance. The core stays free under MIT.

The optional [signature companion](https://github.com/kryptocorelabs/kryptocore/tree/main/modules/signatures)
adds purpose-bound Ed25519 signatures alongside the minimal encryption Core.
It has its own keys, tests and documented trust boundaries; app integration is
pending. All current applications remain previews. Windows executables are
unsigned and independent security review is still pending.

## Build with us

Code review, interoperability tests, documentation, and reports from people
building on the core are welcome.
[Read the contribution guide](https://github.com/kryptocorelabs/kryptocore/blob/main/CONTRIBUTING.md).
