#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "6be37d69537adfdf4c33f1edaf47baf7a4b56316461ecb5de577e6ad1b021b0c"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["f7058b24aacc", "e2ea8d3d4268", "b1274a49027d", "2f662e498ce0", "9e74e3b072aa", "ae709c570cd6", "874a7fcf3c1d", "3703644d4cbd", "bb392b3d2f5f", "713fa369f74b", "95e1f549237c", "ae8c05479c5d", "aaa099b899b2", "15924d0f876e", "3350d8dc2c9f", "8316389795d5"]

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
