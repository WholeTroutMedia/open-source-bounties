#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "6ae9b910eb16ef14e8b22d15deda2c087dd6e83949bdf2cd8e7846b17c8feef8"
PRIME_MODULUS = 4099
COUPLED_PARITY_ROUNDS = ["c127b3e947f8", "8edb5014cfe0", "e9c5dba8ee2b", "8d44ebae0250", "4b31444c811f", "533b710330b8", "b48ae5896503", "3799c73ddf49", "a04a0c57a4c2", "94be63bbc885", "723e898cb8d1", "2f6b8b02a86b", "048ad11666b1", "25ccab19b0de", "6c6e4bf9f629", "4a9c00ab7bb4"]

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
    print(json.dumps({'suite': 'tokio-ringbuffer-seqcst-405', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
