#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "907b7c4eeb6e6a93cb91940cd8981e6a6b56c4eac9382a25b4350077a163c5cb"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["af1c0e479a6e", "40348141ae97", "981865affea0", "7c84a97d4c7c", "0a538bde59a5", "9652f3799f37", "c9c51edaf1bc", "af6fe08d5ec1", "b6e046bd9283", "85126d7b29f1", "22ee2920afe9", "30a4881f316a", "4e242caf038c", "5230c813ee1f", "48f6cffb8452", "d5a77d5fce2c"]

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
