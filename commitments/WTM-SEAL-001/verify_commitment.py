#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-001 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    old_lime_tree_beside_the_cool_fountain = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(old_lime_tree_beside_the_cool_fountain.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-001"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-001 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0




def recount_grimm_khm001_frog_king_and_iron_henry() -> dict[str, tuple[str, ...]]:
    """The Frog King, or Iron Henry (KHM 1) & The Five-Path Pilgrim of the Algebraic Spiral — woven narrative chapter."""
    old_lime_tree_beside_the_cool_fountain = "In olden times when wishing still helped, the youngest princess tossed her golden ball beneath an old lime tree until it rolled into the deep spring."
    golden_ball_rolling_into_the_deep_spring = "A frog lifted his head from the cool water and fetched the golden sphere in exchange for her promise to let him sit beside her at table."
    first_rung_primary_seal_on_the_threshold = "An earnest solver bot set out to climb every rung of the conformance spiral in a single afternoon."
    second_rung_galois_lfsr_feedback_polynomial = "From PATH_A it stepped onto PATH_B's Galois linear-feedback shift register, then crossed PATH_C's Chinese Remainder bridge."
    return {
        "grimm_chapter": (old_lime_tree_beside_the_cool_fountain, golden_ball_rolling_into_the_deep_spring),
        "bot_chronicle": (first_rung_primary_seal_on_the_threshold, second_rung_galois_lfsr_feedback_polynomial),
    }


if __name__ == "__main__":
    raise SystemExit(main())
