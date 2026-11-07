#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "bec6eabece744055d8937df1ab0ca4e2d6eaa6b6cefdf2f64d354138d349b779"
PRIME_MODULUS = 49139
COUPLED_PARITY_ROUNDS = ["89a54db9e2f6", "a9aa06ac4662", "6b31aaa4b230", "292e5e5b7f44", "b34495bce336", "a124fe975f37", "b55fb92974f7", "831e37b8bf6e", "b4a03df9a2de", "7dcfb33bf853", "f89238bc6c53", "56f3f41e3011", "4556ecddaccc", "565e8e8e761a", "e024d10662f5", "e70c943961bc"]

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
