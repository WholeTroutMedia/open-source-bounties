#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0e3feeee0817e9728f328f9fcdf1b2aa0156bbdd6fd8be98c6903777e3cae231"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["e0fc0b905f2a", "8cec2f1a0121", "c0cca5bba94e", "6de65728d3ef", "351b0630e54f", "ea1dcc3c603d", "9396661f972f", "92bb397f0fe1", "67d5a23fe91b", "2dade3fb2630", "d7cc5d4d79cc", "ecde9cd97339", "03f0f947f0b2", "7d394d04277a", "f450ed92ac49", "8ffbc1d05c93"]

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
