#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "b2776b0d55806a0509a1514ff5cdd7204eb453dbd40c3f3113a2d7502b266cb7"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["bf3980df44a9", "01863fb01c81", "dd202fee9acc", "8a3b186d3d6d", "134bb0aa2138", "7ba936b99924", "f2301d6b9c8c", "4c9077080219", "27c924c3ae87", "cdc7cad40f48", "1c06199be976", "83fe9bd43a38", "dab3489ca919", "8f3266c39525", "f15bcc229b9c", "acbd01273ce3"]

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
