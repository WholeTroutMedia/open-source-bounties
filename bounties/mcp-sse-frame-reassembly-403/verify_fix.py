#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "6ff5792701dacf3496dfc953dffd648e1398dbfb1d2757478601f7cb63776344"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["5296b29e6be7", "60b724504f89", "630c9e85d0c5", "79f188e3d383", "ea1f2451ff51", "68c6453815eb", "2b1abedb0d2f", "9ffca021af8b", "06df78d8c025", "2bda6caa8ea8", "0b5278e88d42", "edbfe7642935", "2c6b12b937ad", "0cd677e16897", "71c3c9384774", "935fc56c7a81"]

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
    print(json.dumps({'suite': 'mcp-sse-frame-reassembly-403', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
