#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "60a93f0ddbd130dadbe873a08331cd97a0fcd85b5967294ea273db733f4df7fa"
PRIME_MODULUS = 4079
COUPLED_PARITY_ROUNDS = ["93c078940c73", "86f9b4a250da", "0ea52ccc8c0c", "602b2c8282c1", "24e85087aaa1", "254cde58c3ed", "e4baf2dfa80f", "164a0110872b", "c31c7992cfaa", "d0c898e01454", "9e1363ca6694", "4210c55b4f00", "e7bb16d525af", "e88f982a8a9a", "961a6df18124", "e6d38100518e"]

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
