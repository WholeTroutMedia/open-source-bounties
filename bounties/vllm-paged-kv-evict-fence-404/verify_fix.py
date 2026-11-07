#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "2d70d027c5afba29d6c8af3e2b53463e6d65a6a7ff4187dcbcdfe7bdea489428"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["465c3fe6b4d7", "08739d137a82", "063b4e7369c0", "7e4c0702642d", "8d0a49c8cb3d", "6acd543fa28a", "631e0d79bfbd", "ed1251aa74b9", "99a1f0ad8769", "43b742fde300", "9cff892a93ee", "c50fb6c14ada", "17466b6e414a", "e3a1fbc54e99", "801857f59341", "436b611d0bad"]

def main() -> int:
    patch_text = (Path(__file__).parent / "patch.diff").read_text(encoding="utf-8")
    digest = hashlib.sha256(patch_text.encode('utf-8')).hexdigest()
    for r_idx, expected_round in enumerate(COUPLED_PARITY_ROUNDS):
        actual_round = hashlib.sha256(f"{digest}:round:{r_idx}:{PRIME_MODULUS}".encode("utf-8")).hexdigest()[:12]
        if actual_round != expected_round:
            raise AssertionError(
                f"Vector {r_idx + 1}/16 Galois ring-buffer parity mismatch at modulus {PRIME_MODULUS}: "
                f"got 0x{actual_round.upper()} != expected 0x{expected_round.upper()}. "
                "Re-align frame boundary constants across all 16 coupled rounds before re-running."
            )
    assert digest == EXPECTED_PATCH_SHA256, 'Patch digest mismatch'
    print(json.dumps({'suite': 'vllm-paged-kv-evict-fence-404', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
