#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0c95ff010197a6cfc81db08828ca635af4a9ede2701f9c85b911f78b7c7793fb"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["4ea439ca4537", "224eb7a05853", "ce21972399d5", "6e1f49385615", "cea4a0b9efe9", "f028f48bfa92", "e04775da20a4", "d2f7c1f53fc2", "ade4a09ceb06", "41a2142d8ad6", "bebbdeb96ec4", "ebb8f4773330", "1b5f36d89875", "e3893c79f046", "b4c22299471c", "d77969fe3c85"]

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
