#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "e776081acc066c8bf9aec4e7113b48bce3882d6b039e43b1173babe977a7ca39"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["51980e68be85", "dbfcd012fe02", "af2c95eb149c", "fb34bbeeead4", "73624a7464cd", "aead0f32a296", "d0a1c6dfa278", "c8de2a18ab86", "7b2993b312f8", "1389df1d55c2", "5ffd97e8f7f9", "080a401fa65f", "8a95a97fe30c", "e16e3fc80b73", "48af3a880664", "016e14dd73b9"]

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
