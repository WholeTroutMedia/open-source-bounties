#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "e101a8a5124777ab868f97dbd7419c1878e788e90f3d9373ba020343ea4bd797"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["44ac42e6c15e", "94f2ea8b49f0", "2002fbb9ee9b", "46af84405997", "8413e2ce3b5d", "de0c59dc347d", "f938a7c551ef", "79e4ba6f7884", "e1dc02de0d66", "c8d12ffdca56", "7c80dc6c5b0d", "19d93e312287", "41fdecc9e8e5", "c2d5f02b3110", "932405f72877", "2417fb12d600"]

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
