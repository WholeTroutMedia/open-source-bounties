# Rust, C++ & CMake 4.x Maintainer PR Conformance & Anti-Bot Gate (`02-rust-cmake-pr-conformance-gate`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: Eastern & Central European + German Systems Maintainers (@radumarias in Romania on rencfs, @AdrianEddy in Poland on gyroflow, @ChristophHaag in Germany on OpenHMD, @DerKoun on bsnes-hd)
> - **Stack**: `Rust, C / C++ / CMake, Python`
> - **Domain Hub**: [`by-domain/04-rust-systems-gpu-and-native-cpp`](../../by-domain/04-rust-systems-gpu-and-native-cpp/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Pre-screens incoming Rust and C/C++/CMake Pull Requests for CMake 4.0 policy range compatibility (3.5...3.31), Rust unsafe/unwrap hygiene, and README-only bounty-claim spoofing before burning maintainer CI minutes.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
