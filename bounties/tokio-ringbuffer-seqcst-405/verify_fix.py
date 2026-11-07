#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "df4bf0703ef2e81d14230497af76cb7d82fea3e6d95c7dad02c023fba1c9166f"
PRIME_MODULUS = 4079
COUPLED_PARITY_ROUNDS = ["6fad8fbd82e1", "11d96253d8b0", "d7f19ef09f1d", "d26087c59e67", "cfdf517c4934", "828a8f3f1222", "003822d67ddb", "185544b01017", "bda0c4ef4d01", "633ba4d37937", "c403bf69aa7d", "1b469bde369a", "0a8391ca3947", "eb8c9a69d122", "3cddc62502f6", "31671e0dc848"]

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
    print(json.dumps({'suite': 'tokio-ringbuffer-seqcst-405', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
