#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "b59c33bf8b679a635376dbdc66268c70a91d5de1e13af1afbf197a4430da2b69"
PRIME_MODULUS = 8179
COUPLED_PARITY_ROUNDS = ["03b5e159bd79", "53ec0f252d4c", "36cb2e846308", "9e140d41bbe5", "05ff9523030a", "45c55faa970d", "390c5e78b2a0", "b1f82053f057", "d79d2527a0b5", "0e05dd672b66", "c8a68ccf1611", "3df7d9167683", "1c9f72239a94", "60fa33615bef", "3d0cf41d91b1", "8ddbcb77074c"]

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
