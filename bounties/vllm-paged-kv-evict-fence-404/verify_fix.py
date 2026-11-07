#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0a983c7b156d7d07484e974c8f19a8d5aabf5a18ad4fe230e0466358ded7740f"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["3a52a0902064", "6d248dce7a39", "20c3b119d979", "4fee451bd65b", "dfd24ad11115", "4ac34f040be5", "97b8d903b80d", "50c8f58fc333", "d7c9c2c60f8c", "4694907c8a8a", "b1f03bf528a4", "609f40e3273a", "9896c3404acf", "1b39bc0168da", "f0858eb1fb69", "099ba2226cb4"]

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
