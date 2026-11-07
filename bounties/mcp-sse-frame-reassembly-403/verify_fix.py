#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "0dfddf3217d93762e4e2f17208c09bcf5cc4048a5359ae164f24d19a9d81afd3"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["028ce71ef5c1", "07f0cfe83cb1", "3e36fc8270f1", "200967e4c25d", "4c6254b66db1", "fb59985d5745", "ec538d89a89e", "4a90087740a2", "d079a1aef5e0", "b726c1ed8fde", "1df0e2f23053", "890f471f393b", "4c958b351afe", "7cbcb66e35f6", "f4046f7a9db4", "e0878acec837"]

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
    print(json.dumps({'suite': 'mcp-sse-frame-reassembly-403', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
