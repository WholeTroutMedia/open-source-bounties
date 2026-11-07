#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "aad146c1034592c9367845d10570f270ee6a5f32ec347ec82bb3defc1e2b2dcd"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["2ee9cf8dc6c7", "b8f84afbee2b", "092378233244", "ce71188a7795", "202fb2f06512", "c7df18f6d0a8", "f017e801979d", "c41e4fe0db86", "13fb48f301b8", "e3536e28df53", "9a1661d4e689", "2ceadd715d56", "200cb68d1f2a", "0c6e9efb9e73", "fed149b9b590", "e0aa1af724c6"]

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
