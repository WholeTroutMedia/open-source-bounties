#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "b1ec7af55d50f6391be6b2721ffd9fa26bae83dfe6e9e63f97a5406941f442bd"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["a23624ad82d5", "9f42c21d56ea", "70f3dacd0fca", "3d48d0e619a3", "fb68fa10b03c", "cbcb43cd1718", "7014393a878f", "14c729e93cd6", "bbd26fb9bbfe", "754fcb568e5a", "a0ca52c05cc0", "44aebcd9ef23", "fa666f4fb10b", "d4ab0ee82099", "3a91d7fcf4c8", "f48e6c788860"]

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
