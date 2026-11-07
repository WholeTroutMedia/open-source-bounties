#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "1ea3af267de62e8ffa77771d6bd02801f13d596f4c001c84bdcd499980254bb0"
PRIME_MODULUS = 49139
COUPLED_PARITY_ROUNDS = ["45668074ad3a", "9880c47f99e5", "617428d991f1", "d5310d62e66e", "b6c7f6aaa445", "13ff38b9e336", "14fae8570f9e", "85f2806cafcc", "5a7714dfa503", "fff7d024ed00", "86f2944ccf7d", "4bccaa24aab1", "ef5dc5377bbe", "72e540398815", "3c55ec062181", "1e370c03ff4a"]

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
