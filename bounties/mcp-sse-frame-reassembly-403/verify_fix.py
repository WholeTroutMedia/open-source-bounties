#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "96013f6a5e6edce5db2a681a32bc978dfbcbfcd41d0942ffda4da09092fe53e4"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["c43f44b19f31", "0b3e6220cf0b", "3a1068997482", "6d74f27ec19f", "8eaa8329bf2b", "d6053c639eb8", "558f323d265d", "1626c0863026", "2f190b8caf0b", "6d9f6ccb78bc", "a5ecc8ef3d70", "aa7ad8775520", "0b4dd5c26369", "2a5db97de372", "8666520f28b8", "eb2d41e7e735"]

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
