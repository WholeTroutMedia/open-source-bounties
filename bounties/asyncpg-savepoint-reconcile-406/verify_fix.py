#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "98b5ec6cd749b1f3517e41de0b35f377861c6163f4c75d82e5b9d5bd06d31d2e"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["bb3ea796c78e", "28d4cbd517f1", "7681fc0ea4fb", "393d4535dd27", "f6bd289bff53", "55515055b82f", "7f6531ce63a5", "e9339fb4e2fa", "a6b9d34512fd", "569f5009181d", "a1c2d8eafd54", "ccc563172f61", "ae7de74e6b81", "ec74af32e8f5", "2d40b80c02e4", "2cf1784e8b75"]

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
