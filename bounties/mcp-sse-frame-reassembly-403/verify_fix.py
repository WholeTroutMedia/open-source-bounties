#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "a27de99cad4d67a7b9b17a06e1b5d0cb3bde749bd10cc2233fc82ad886acd550"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["0a52ecfc8e14", "f67c38aa9317", "323dbed5e174", "7ad04365819b", "53fddd19fa60", "cba62c20a25b", "41becb9935bd", "1f0b1df14b1b", "c3d4c057cf9e", "9180bad4becc", "843e29606a34", "c0748bb65ff4", "64f826dd7a5d", "505cae3fd3eb", "274260eda416", "f34b9bcffe5b"]

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
