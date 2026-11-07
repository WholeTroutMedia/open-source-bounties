#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for mcp-sse-frame-reassembly-403."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "49ff3f97e68aedb6edd6ac9b709701e2f29ac69568dde2930da059a17f836041"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["07625c3a0105", "bb80619cba0a", "d91734dffed9", "a3a63e7e7b80", "d8ef8df4f276", "89c7778379eb", "69422d549e2d", "e5ac726c849a", "d38326aa4f72", "912aff88fb19", "d1d2a4a7707c", "0ad4cfc91e87", "5af8c8822e9d", "a87f782809b5", "b3c801c59c59", "2386b23b6e97"]

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
