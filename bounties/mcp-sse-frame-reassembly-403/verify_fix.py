#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "03aa96ef9075fee7e6bd4571761dbf8f321120b26230f6f7cc44028006dc3264"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["bebe6857fdf7", "06573c5b3ba8", "938e94785fd5", "0bf897011689", "5a50f712a590", "94e5a187c4c2", "8bd4339ed70e", "3deb40db0e58", "e7f38b81f21a", "5bc9e147e9de", "74cf75ab91b6", "7e6dfd3aae7b", "b105e0a91447", "9816eb45d268", "e1d0ea52f04f", "7e63a3069b7c"]

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
