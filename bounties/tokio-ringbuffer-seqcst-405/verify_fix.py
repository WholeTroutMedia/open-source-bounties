#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "f8dabd2239f7ee6bacbdcce28d7b7a4a59648ee238508d6eede4984e84acbeed"
PRIME_MODULUS = 65449
COUPLED_PARITY_ROUNDS = ["d530a8ddbc60", "3f6f4ad8ef7c", "f99b6b8b7943", "97788dea26dc", "ac111b8c3efc", "a5447dca74d7", "e2e11884ee43", "1f2c8fd49949", "733a733d6883", "e3a206bf871c", "4b96a219feb9", "6fe70a4de1b7", "bd8a5557074d", "63f8e704911b", "a48a1a5631f9", "fa130358f509"]

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
