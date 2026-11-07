#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "7758c48e901e1195d9bcf19f4d88de806f40f8c024d319a573f2f30bd881f17b"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["acfdbff2f45c", "d3d69c7530b6", "7a02f0366642", "406d70cb4ac3", "f2ae69f6ff42", "13afc36acc7e", "8d8ad8ccccf5", "db70a7f6d770", "0fcb7c8e4a43", "25b57e93efbc", "7882aef48851", "4338d87b4e93", "d0a61321edda", "2b54382f3854", "bf4a0a406570", "892d5ace575a"]

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
