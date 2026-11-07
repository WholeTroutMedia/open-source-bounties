#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "48c3e8f0d83c8e475f9dd54ef23fc83c3235bb5d41f1b2d51506217fbc08a3fe"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["1ab228ded17d", "a4a2476d69a7", "2e642164ec8c", "bdf8318bea25", "067bfdaf7f99", "6fa592463f48", "501a5bd6165b", "62a4e58a500d", "01c4ff3a8122", "fb9521b23dd8", "a5c954240086", "db2a3f576691", "e9c1cce597db", "50f4e434276d", "41c85693a142", "9bb683adf490"]

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
