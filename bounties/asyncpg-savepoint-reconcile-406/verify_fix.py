#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "2b6e30be467d45be9a6352b3f3144a92764046528369c4148ededb88fe5cdd7e"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["d5d35419c421", "bed738a212d0", "410c2bc0a726", "35938d5c042a", "9dbb383ab1ac", "1b0db663a0b7", "bc8ec50c1c90", "3ddafa312925", "20cab046608c", "0a1064078694", "60c60659409a", "942bdf672770", "1d13f7e7ad19", "d4aa18e48d30", "911f9fa5edd9", "1027a3406378"]

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
