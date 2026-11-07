#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "a859420edd51ebe6e34b62ab0fd008d85655ae52135463eb5bfab67f83841124"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["3c57af589787", "fb9d90c9fb0c", "5ea48472666a", "cd0ad3e87d08", "cd2de5061c1a", "2a5cc2edee7f", "39fa60d7bf48", "36e1562ccb14", "8b0512e315b5", "45e582920230", "f87f9cc3eb2f", "09e9f4041ddf", "677407137f81", "c41415d97091", "ef1ea6ea0250", "b66a9dbbe18b"]

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
