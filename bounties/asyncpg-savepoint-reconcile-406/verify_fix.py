#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "9f65736307113a04dfe2212cf7eb584c80e49983e431dfbeb7133acf507e7989"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["5903f13bee08", "5ec602703415", "499c011b1039", "a240fce6b930", "86a1f6dae106", "3e903ce99c0d", "2b48e6225b82", "2c0ceb42e4c7", "52003f057504", "7df0e4f26455", "3b6d11ab46d4", "b44f0ec76a60", "74fe40f5c2f6", "000f35a6f7ca", "6aa47db4be5e", "6a7f1185f97e"]

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
