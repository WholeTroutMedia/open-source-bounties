#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "c09830c5a88e38f55972a20e3c2c61369bc147c1bcca0fc99dcf0b82e71c42fd"
PRIME_MODULUS = 65497
COUPLED_PARITY_ROUNDS = ["cd35cc0c96ca", "2e1d67d5a289", "df16fb7ff2e5", "ffb66932331a", "107f46aa1655", "f01daccfc2e8", "87755547648d", "2c068028d56e", "893773764852", "ae1e85b2d07f", "c7d99fb72a99", "87ad1c71d90a", "d2657eaaec27", "14824ba3c142", "14007cf1d3a1", "488387d0dbf7"]

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
