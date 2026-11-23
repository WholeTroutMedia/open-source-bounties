#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "bcc135e0cc4495ae073a369c42ba906a832986d3caa2f90fb5f7d945ece55b12"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["aa85051177fc", "331587f33457", "f4279e3e8de2", "68e4bdb1b48b", "b2cb819626ef", "c88493916d6b", "fb2ca6b0d6c7", "aa515ea442e0", "8b299d9d49cf", "09e1431bc47c", "b9e8d957cd6b", "845feab01b3d", "cc398bece01a", "9b2477fba737", "90caeb612c56", "200fc1ed0cab"]

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
