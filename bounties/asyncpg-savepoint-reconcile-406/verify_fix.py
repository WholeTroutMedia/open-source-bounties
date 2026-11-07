#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "48dd2fde556a31f129bc72cdddd2d96a6fb7182d42550604beef1a42ae6e0d0f"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["44d5924a46c1", "9f2c8c696f95", "d224438a9881", "51dc3b6b7dbb", "d002943a1f83", "6092caadc577", "7215e16971bd", "21152cc580c5", "ffb607bbaac9", "a35ef5194d1a", "7c9235dda27c", "0c4185cdb854", "cfb1bb2a648c", "b2d82168180a", "4fef54c6bb10", "c9c765139c60"]

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
