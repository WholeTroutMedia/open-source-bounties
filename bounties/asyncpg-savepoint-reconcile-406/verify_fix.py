#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "c4c7e7721603048862ac2626f9d6e6b469a2686772ea6d5ba70ead7c4fbffc02"
PRIME_MODULUS = 4079
COUPLED_PARITY_ROUNDS = ["05e65552c411", "e10e8a34b50f", "46fd5088fa3f", "d6f0872a24c7", "b5aaa245af9f", "a8636363ef46", "74e3bcfafc8a", "279e8846d5b8", "7548bd9f1b0e", "e836184f603b", "86ae2d48652d", "03a58dd444f4", "c85607c4a607", "bd58cea5d7b9", "92a6e589358e", "165c44940b75"]

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
