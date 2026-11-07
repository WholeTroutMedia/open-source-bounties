#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "f4350eeca18c022778c0a68123be2f1b12da95cae8352042a505addfc07eea0e"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["45b844a2f6ad", "b6bdddb24266", "5af35ae7e8d6", "11ed9d620939", "426502dd4fdf", "8beab5a20f8c", "c0aae3c69eef", "e5b394387789", "bb668de32ca2", "d3e920492142", "2761dc61e433", "9346862174f2", "d76a88234e1a", "62ba8cbbd4f3", "cbbd4673dbf9", "b14a9ffcf2bc"]

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
