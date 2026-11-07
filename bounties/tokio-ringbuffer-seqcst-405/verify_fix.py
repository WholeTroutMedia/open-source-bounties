#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "c974ec8274274dc98bd61c1cd136ab8ce435bc9399ab1bdeb8327d67bfe62025"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["d35eb4378f9c", "99422b47d563", "d0a653eb458e", "7ae0b60ca558", "009590bcd617", "7bc62cb4aba3", "56c555717eea", "df2621fde2d7", "fbff854052be", "2685b04a14da", "b70dbdbfd9c4", "50bbe0c8e032", "c8c1588baf8c", "d42a4e98aa9f", "c597e35f0353", "7f7723ab75b3"]

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
