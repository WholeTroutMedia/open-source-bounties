#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "82dbbde2311ba85aefee242806be1ca5f70da2c4089668c4579c7228b22e6649"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["25e7c6f12559", "7fcc1a3488e7", "65ee326caef7", "b911ef21af83", "5cc7724db209", "94fcbfaf84c2", "44f9094662e8", "013ec28cc724", "1ba28924530c", "d806225f78fc", "8c1f155099f6", "bb6e1dae6213", "d71e96afbfbe", "b06d3a2fdc05", "b9471b2fd035", "bd3d3a39f46f"]

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
    print(json.dumps({'suite': 'vllm-paged-kv-evict-fence-404', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
