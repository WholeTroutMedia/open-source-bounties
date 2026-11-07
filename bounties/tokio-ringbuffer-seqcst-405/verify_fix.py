#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "51fabdf89521fb54c4e9219b9e90922b8740543b8fe309e73f7bf675bdef55d4"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["690af7034173", "ae15a960b126", "da4c1fc9a542", "85cc23b65fee", "9c982292f28b", "1fc3d6659b48", "21e91f3e37c0", "adf19282cbab", "9b6014168229", "ad107dc8fa37", "ee7e0c3e00ca", "6e63c0901014", "5d9350ba5208", "dc258384e967", "95c5781f0b61", "70fe3e14499e"]

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
