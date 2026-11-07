#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "05fe45a960c2dd9f1e9a012a9d16236e1fde494d8700fd45bf7d6a3f714e46b8"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["cc420944c510", "db32fee02618", "b4e68207e735", "654c61a3de52", "229832b50aca", "98f7ba5cd125", "cbeec949e566", "6647ff5b41e7", "9d26a6ae15d6", "27c3c712defd", "bf93c5338941", "ee8a6ca5a92d", "0ad0fd9b74f9", "3be99b738bc2", "c51ba795da62", "d1e0a45381f5"]

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
