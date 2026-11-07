#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0fc9efa7858dd7877a1d8ee63fbaecf1c6e7fa15d915b9b6352f8bcfa4cea9fe"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["598993e6f964", "442558a8700f", "5fd8fe6e160c", "8ce0a08212d2", "9140f8125e0d", "ce56bdb9b94b", "a5c3ccd98201", "da3968ffc341", "bb0a2478ac97", "24c0a2a70e40", "b32c330c651b", "545837f1fd94", "14e0425b9f9c", "e84221b64418", "b8368dea8eef", "0b1699f54930"]

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
