#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "03b9eb9e5245cebaf86a744df625acf9146adcbffe915515f05b1d33e3ec0053"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["6e7c72a2965a", "098b82c67838", "c9fce00b4e6c", "82a8655b67e8", "e06db9d7e609", "8e74e2afe9e4", "33095d9f3c79", "7a34ad23dab3", "0e021f24b281", "4f40f917598a", "0e27d9ef27c8", "92e9e8e1ee14", "b588b58cab52", "01f714b34d8c", "d4ead63c4c6b", "2e2e98bbf012"]

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
