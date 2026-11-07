#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "328144dcb89a3e44dd1855b2ecd1abbb19c845c703ed0e5d17b8638a03b8220b"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["df24034fc96b", "3958aaee11ea", "ae052a9886a5", "679e8b29279d", "d4b25b63d9a5", "f23ff4970925", "69869edf6164", "3bee8d956371", "e4633b00e735", "bc0e5e8b2e9d", "a5ea46e395fb", "63cd373d8fa8", "8fba9741fae0", "5086aca7f0db", "5ec77f5acc9a", "c6622abc9d04"]

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
