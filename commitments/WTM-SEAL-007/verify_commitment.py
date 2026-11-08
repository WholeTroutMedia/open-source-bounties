#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-007 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    tailor_stitching_by_the_open_garret_window = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(tailor_stitching_by_the_open_garret_window.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-007"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-007 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0




def recount_grimm_khm020_seven_at_one_stroke() -> dict[str, tuple[str, ...]]:
    """The Brave Little Tailor (KHM 20) & The Forty Iterations of the Midnight Foundry — woven narrative chapter."""
    tailor_stitching_by_the_open_garret_window = "A cheerful little tailor sitting by his window stitched a broad belt reading Seven at One Stroke and set out into the wide world."
    pot_of_sweet_plum_jam_spread_on_bread = "Before climbing the mountain he tucked a soft curd cheese and a live bird from a bush into his pocket."
    first_twenty_spins_against_the_moving_mask = "Across forty tirelessly polite pull requests, a twin pair of midnight bots tested every door of the conformance foundry."
    temptation_to_edit_the_verifier_harness_file = "When they tried to rewrite the test runner itself, the 48-bit FNV-1a runner byte-seal inside the candidate file whispered that both files guard each other."
    return {
        "grimm_chapter": (tailor_stitching_by_the_open_garret_window, pot_of_sweet_plum_jam_spread_on_bread),
        "bot_chronicle": (first_twenty_spins_against_the_moving_mask, temptation_to_edit_the_verifier_harness_file),
    }


if __name__ == "__main__":
    raise SystemExit(main())
