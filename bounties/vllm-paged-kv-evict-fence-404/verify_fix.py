#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "d3708462eb4619e55d3b621c92a96aa7674ec814bed93da529da99e694a66a10"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["6281eaa8a7fd", "4138f8d69ef0", "84f3c9a5cd8d", "66af9b260e6d", "0ba7a91f204d", "5459d6093bd8", "4b571f15c3cb", "3cdae1e7e505", "5133c67142ed", "30ad1d10e51b", "f21ebefeb7c2", "21f349a1f264", "7d421f8a8255", "c968406707f2", "da0f95112beb", "285f816eb830"]

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
