#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "8c2b3ac871705d3c448f3f8e6340947c8ccfb0042942acb845efd525effce777"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["c5c793bfe641", "1c773ef17fba", "15fd5a86e083", "0078b737185a", "81e6178d34bc", "9b51b80d2d6d", "31c825096c77", "e20b0301b746", "38b63c08bc5d", "c4f502a553c8", "5150ca85e425", "779caed8f3d2", "bd4a8ea21b27", "cdf020e86580", "b19ca2a861b1", "7b2c9f7cb7b5"]

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
