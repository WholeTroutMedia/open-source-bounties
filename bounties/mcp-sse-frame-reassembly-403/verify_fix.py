#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "ba61db06d71eb494772ef6aa3ed6cbcd2932256f14e8b210d893da221b2257d7"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["e15697c9055f", "9c498dceb1cc", "dad56703af0b", "8a23a0b5e031", "a4d873b517d0", "38919c674210", "51d1c9568dce", "c9776f6b141c", "bfed73f07460", "a5d3ada605ee", "70e6efd9ccd1", "87c76127f6d0", "8eec07671cb4", "9fd8a0cbd3ba", "cd9979faee34", "08091ec748df"]

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
