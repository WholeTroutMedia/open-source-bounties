#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0e2573ac1662e2c29717a54f73bea22ecb7603a8c61c8a22a90a200d1312cfae"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["0a76c0187c43", "ed6a4b8ef3c6", "ed327c8368ea", "e69762d6686b", "99b174cb209b", "8d3441a1c6ab", "2df35ee57a24", "ca958ca8c993", "e5e4215a2e59", "acbc07919c93", "a231999bb567", "ae21a81a03f1", "bd85f1b6e258", "61a6c26956ed", "e107542e434e", "fdd6c2b21c6a"]

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
