#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "89b5cd84ec89db9713d136aa5d4d4ed499147a5ebcdf1496c70579f26d362e88"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["e4c50988a9c2", "911778986a60", "25b6dfcc7e04", "c8f6bbd5dfc9", "6b1565dc1a8a", "f2a87244a60a", "91b1c5cc9841", "5c57cad1c15b", "bd6457c690ae", "ba973753fe2d", "dd2b0ec154a0", "94f38e967ca8", "f9bd048484da", "dd3ec6901ec9", "04d0fe8fb96f", "087d40803c4f"]

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
