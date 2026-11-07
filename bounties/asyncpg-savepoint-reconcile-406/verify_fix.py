#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "41d7b9237ca408226968facf5a54b18ceb7d7d59f8ab5e2140189801f535be25"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["89db588d8a28", "b372ddf6fc35", "e17530437dd1", "18f86234ca73", "557d16482c38", "babb504aa28e", "ad158b391464", "31823ea816f9", "87b7da260f15", "de42ab7139ac", "0ceb41932f31", "c35482ab3274", "d215a2670e69", "c9f634af2b9e", "6de08ae62e37", "001e72799ede"]

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
    print(json.dumps({'suite': 'asyncpg-savepoint-reconcile-406', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
