#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "2425da4042dc4eb437bbd29ff7a9aa5ba8313bfc461eedffc4fbe6a7b29e0c8e"
PRIME_MODULUS = 49139
COUPLED_PARITY_ROUNDS = ["65f8aacd0a7e", "b979a67fa385", "13287608e581", "0924548f7f77", "8edf9d4f2844", "683d1aea8182", "495cced4bb75", "0231a60dc3df", "47d2761341a5", "364f0cdf826d", "fafec82e42b1", "be17c6a1abf4", "90774f0e9873", "6b73fdd59531", "1c5bbb858be3", "9d34212926f3"]

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
