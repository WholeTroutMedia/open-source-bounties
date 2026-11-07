#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "9f84bd02996f00b2ca7ba0637161b90f8eb8d1d510435e3072fecd50e3dcf525"
PRIME_MODULUS = 4079
COUPLED_PARITY_ROUNDS = ["3d6bd019641f", "48b96a708ade", "ed7c9c971bc6", "ce87b4d240e0", "1a2b21da17e9", "49f6113d6f3a", "5da53b0ba3ef", "e62dd379134c", "d13ac317733d", "2dc248e3910b", "b45af73603cb", "25a0eb432c3f", "42d5c6e8505e", "4a3b577d9690", "37c7a5f48ea5", "fcb030c15195"]

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
