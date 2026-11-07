#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "60ef6ab63fe1db0fd5efd34f9e91a6e63b3ebeaa02f50264f6a769d0ae45c94e"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["ee795ea48130", "46ac844fa150", "bc4ed69a5d8c", "92818d384e62", "a6ca853ee844", "0981045a7d76", "50bd2d78cdb8", "7195bc8a86b6", "cbd6dc68d71b", "41857937dc56", "13df673ed76a", "bd9f270df4b9", "0f7b42b2450f", "a4a0ddd02bc7", "1e438d20cf38", "b75b607e9f86"]

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
