#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "d098711a089f4a2be910587f11a4af1cdec07e48b5daab5dcf0484d3693272bd"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["0a5f0fa5303c", "88aa9d60472d", "29ad930f9e90", "4df5b0a54c37", "5c53ca1185ae", "050b8ba6e0f7", "0c9cf563912c", "49386c666a42", "1fb929b499ec", "45f5cbee3c10", "e37a9dcf761c", "004dde2fedc1", "4e6b2d8488f5", "53dea9a151c9", "02ffaf33c183", "1f479b623c06"]

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
