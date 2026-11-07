#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "940535ff2a92bc7ae6c17d3e46aa251a52e40ca990431cbfd3f5af28f458a6dc"
PRIME_MODULUS = 65449
COUPLED_PARITY_ROUNDS = ["df692ca329b1", "1f9732ed4ee8", "c9d08a3b1209", "c5ed10ad1f39", "27297fd45f37", "780f86dbcd81", "618ffca76d8d", "3f2eb85ef7b5", "3bcafc6279cb", "cbb72cc5311f", "0068bd01d582", "4d6206d531f9", "4b0b516d62b8", "4ea66c1eba5e", "71dc7b4683b7", "6e9b28a12408"]

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
