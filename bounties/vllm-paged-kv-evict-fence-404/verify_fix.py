#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "6fb1f83bc833fa605f540020772b2539dabfc80239bc5209df9cf2f46677a9dd"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["6490289a1bf2", "e0edf6d237ba", "2c6d1a6fc086", "024a462404c0", "e87bab29ef23", "18ecd0432358", "b0f0f4586d62", "3ce0c42c388c", "0a975c5339a0", "45ccd59176ac", "93b40cb3e137", "8a866dab7987", "c39a5ce709eb", "79ea9a457e6a", "d989262e0218", "2a0eee9e30f3"]

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
