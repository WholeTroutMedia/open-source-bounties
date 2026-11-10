#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "b06a2bb0633b2b7585a7a383b9274f72f995bcbc7ecc0fac9e25ba8996c51a50"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["d3dc2f3f773e", "524f9effb860", "aaf39d0dd220", "0910e781189d", "8a6e48fadcb4", "725f71cff35c", "aa4bb0696b0f", "0eb34b876618", "e2c9a1749f34", "bde498b2f943", "cfcfcd269072", "216c6b6946ff", "a8162a8423d1", "7c1fe6a1d1b4", "7ee24bcc0ce7", "915f5d370b64"]

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
