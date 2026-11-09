---
name: 02-rust-cmake-pr-conformance-gate
description: >-
  Rust, C++ & CMake 4.x Maintainer PR Conformance & Anti-Bot Gate. Pre-screens incoming Rust and C/C++/CMake Pull Requests for CMake 4.0 policy range compatibility (3.5...3.31), Rust unsafe/unwrap hygiene, and README-only bounty-claim spoofing before burning maintainer CI minutes.
---

# Rust, C++ & CMake 4.x Maintainer PR Conformance & Anti-Bot Gate

Run `python3 kit_engine.py --self-test` to verify all deterministic invariants (`Exit Code 0`).
