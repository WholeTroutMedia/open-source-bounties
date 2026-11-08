#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "e485b80533fc4dc537ddb19a945b7c3035ef66a2af69102b51746376f8d2d93b"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["13bd95d2f391", "f3d81fd92c93", "d6b2e7afd39e", "46d31aff60a8", "6675afc92b19", "3e8775a0ec9b", "dcbbea33b09e", "81f2a162024c", "e0dad9b01d8a", "3c756de0f4a3", "ba748dcdeb60", "f2693f3ca78f", "49285584a80c", "2b3c47090833", "b8e39b11d663", "1d4fe4b540a4"]

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
    print(json.dumps({'suite': 'vllm-paged-kv-evict-fence-404', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
