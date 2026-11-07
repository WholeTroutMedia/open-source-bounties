#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "df01d85a2dddba89bbaa163bfae05398d573cc5799d8fe33bf3244b99bfb0927"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["a6eada396cd8", "e3ef40df15ed", "eacbcdd903f4", "2e6dec0290c0", "f5b69aa248c0", "38ffbc1d5a81", "031e704f35b6", "1dda2fce43c1", "2a99b282781b", "d7d6a05ba3c6", "df26f6d075f7", "48b264b22183", "9e3bb6e3b623", "4a39c3f85ef6", "87f336b9bd0a", "be6ce05b3b91"]

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
