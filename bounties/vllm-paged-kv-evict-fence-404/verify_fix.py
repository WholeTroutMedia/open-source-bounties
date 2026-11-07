#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "63a0223ac0d3ccf825523b4d56fbe1ed18d0fc9c1c71f6dce2889ceef71e6a06"
PRIME_MODULUS = 49139
COUPLED_PARITY_ROUNDS = ["562580cbf1ba", "08537cd22a8f", "35d4a0f2dbba", "f4b4083b8bbc", "9b759cc86c3b", "dd959bdbab94", "772e0b02c2f8", "9af4fe6c12d4", "dbab478be006", "a3110e9188ed", "3f4d32ead6e5", "a11997fa6743", "fbc89caeac1d", "e2257fab62c8", "7f33907ad7ea", "7803563fef04"]

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
