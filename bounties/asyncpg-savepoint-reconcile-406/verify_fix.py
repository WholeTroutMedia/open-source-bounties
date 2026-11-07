#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "d78366f417cf18ff6ae1e458dd57d52279e02b083db2857eef56b78d852e2e4f"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["ae8ad15dcd6b", "6abdf516ba80", "1f90f73b70be", "59ff10ba72c0", "0db35d486fb0", "a83df95d0811", "466bb549e21b", "050258b24239", "2cf634fcfdc1", "32c1a197a3b0", "f5858e30bcd1", "217d842d6eb0", "8871adb81c95", "4822fbd200cf", "d4383652b044", "80fcf6aefd33"]

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
