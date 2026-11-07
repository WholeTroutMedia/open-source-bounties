#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "6b7c925cd124780f4d0a87bf12a0b82afc3e8754513b664568a2f14a3c6ae42e"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["a641c5f801fe", "fc9b19f3c336", "c348a48e0550", "9c49876198c4", "a655ee82d9b1", "ce885dbe5734", "7cd37b5cde1d", "e9277f00c88e", "44aebf6240d5", "edf1f22c6967", "d4e4b39ebda4", "1c2cb1b43cbe", "dbae4bda3425", "56c09d65adee", "e9a12b4de319", "4c8c2579b920"]

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
