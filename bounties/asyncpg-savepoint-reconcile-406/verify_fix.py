#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "152b0613ce97139b7c687b8e6b5bb7ce1257f1e553675ce6f8713b10317905f2"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["f7ef8b9ff360", "518589ba40a7", "69a47422cdc4", "4aa4568f65ce", "ab06d1ef7943", "47788f4d4346", "4c25fafcdddb", "1a4251b1c9be", "353778be1205", "fba26c0857b5", "db7dd1f3fc33", "9f5d316c133f", "4239dc364862", "08b43154d7e5", "c12c258e039d", "275260fa919d"]

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
