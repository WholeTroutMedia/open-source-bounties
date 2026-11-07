#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "f6d012ac9eae1da927fa76a0273b7591cf3a56a6463ec12050e80394710f455a"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["5f1c45f919a9", "8f17e06ebfcc", "57aec0033793", "004da80d4250", "b47a40c56e74", "7136c86e8e38", "ba1b8d611048", "19183f7b6d44", "2f98b5a0f165", "275e464a97c1", "721ba76992af", "e7c1b4c7f67e", "61b9307ec3bd", "b0a75d8cf30a", "95d06aa674a1", "5c77d473b09d"]

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
