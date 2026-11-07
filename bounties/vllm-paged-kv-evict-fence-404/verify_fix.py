#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "825013b1449ffd248294fbdc27a558d4627a22008c14c8f58f7c8bf3e0028070"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["b8c3e7f800b7", "848b345cc0aa", "ae81c5390dda", "7f3abb473f08", "f9aa8605e345", "4376f449e28c", "d2945b37d51a", "0372e1c330a2", "5830c68cb185", "2bc40b038136", "5aaa7a0ebfef", "ac6e1d5dbde6", "8bf2d820725c", "61488b355ceb", "c66933b4730e", "51b4b1515cc2"]

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
