#!/usr/bin/env python3
"""
Rust, C++ & CMake 4.x Maintainer PR Conformance & Anti-Bot Gate
===============================================================
Built for systems maintainers (Rust encrypted filesystems, GPU video stabilization,
VR HID drivers, and emulators) to automatically catch:
  1. CMake 4.0 breakages where cmake_minimum_required(VERSION < 3.5) lacks a 3.5...3.31 policy range.
  2. README-only or comment-only fake bounty claim PRs.
  3. Unexplained `unsafe` blocks or `.unwrap()` additions in production Rust paths.
"""
from __future__ import annotations
import argparse
import json
import re
from typing import Any, Dict, List


def audit_cmake_policy_range(cmake_text: str) -> Dict[str, Any]:
    """Check whether CMakeLists.txt uses a CMake 4.x safe policy range (e.g. VERSION 3.5...3.31)."""
    m = re.search(r"cmake_minimum_required\s*\(\s*VERSION\s+([0-9.]+)(?:\.\.\.([0-9.]+))?", cmake_text, re.I)
    if not m:
        return {"ok": False, "reason": "Missing cmake_minimum_required declaration"}
    min_ver = tuple(int(x) for x in m.group(1).split(".")[:2])
    max_ver = tuple(int(x) for x in m.group(2).split(".")[:2]) if m.group(2) else None
    if min_ver < (3, 5) and (max_ver is None or max_ver < (3, 5)):
        return {
            "ok": False,
            "reason": f"VERSION {m.group(1)} fails on CMake 4.0+; upgrade to VERSION 3.5...3.31",
            "recommended_line": "cmake_minimum_required(VERSION 3.5...3.31)",
        }
    return {"ok": True, "min_version": m.group(1), "policy_max": m.group(2) or m.group(1)}


def audit_rust_diff_hygiene(changed_files: List[str], added_lines: List[str]) -> Dict[str, Any]:
    """Detect README-only spoof PRs and unguarded Rust unwrap/unsafe additions."""
    code_files = [f for f in changed_files if not f.lower().endswith((".md", ".txt"))]
    if not code_files:
        return {"ok": False, "verdict": "REJECT_DOC_ONLY_CLAIM_SPOOF"}
    new_unwraps = sum(1 for ln in added_lines if ".unwrap()" in ln and "#[test]" not in ln)
    new_unsafe = sum(1 for ln in added_lines if "unsafe " in ln and "// SAFETY:" not in ln)
    return {
        "ok": new_unsafe == 0,
        "verdict": "PASS_SYSTEMS_HYGIENE" if new_unsafe == 0 else "NEEDS_SAFETY_INVARIANT_COMMENT",
        "code_files_count": len(code_files),
        "new_unwraps": new_unwraps,
        "undocumented_unsafe_blocks": new_unsafe,
    }


def run_self_test() -> int:
    legacy_cmake = "cmake_minimum_required(VERSION 2.8.12)\nproject(OpenHMD C)\n"
    fixed_cmake = "cmake_minimum_required(VERSION 3.5...3.31)\nproject(OpenHMD C)\n"
    res_legacy = audit_cmake_policy_range(legacy_cmake)
    res_fixed = audit_cmake_policy_range(fixed_cmake)
    assert not res_legacy["ok"] and "3.5...3.31" in res_legacy["recommended_line"]
    assert res_fixed["ok"]

    spoof = audit_rust_diff_hygiene(["README.md"], ["+ Fixed encryption bug"])
    assert not spoof["ok"] and spoof["verdict"] == "REJECT_DOC_ONLY_CLAIM_SPOOF"

    clean_rust = audit_rust_diff_hygiene(["src/crypto/chacha.rs"], ["+ let tag = cipher.authenticate()?;"])
    assert clean_rust["ok"]

    print(json.dumps({
        "kit": "02-rust-cmake-pr-conformance-gate",
        "status": "PASS",
        "cmake_legacy_caught": not res_legacy["ok"],
        "cmake_range_verified": res_fixed["ok"],
        "readme_spoof_blocked": not spoof["ok"],
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rust, C++ & CMake 4.x PR Conformance Gate")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
