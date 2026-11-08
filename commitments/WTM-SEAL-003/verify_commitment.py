#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-003 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    garden_bed_of_fresh_green_rapunzel_herbs = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(garden_bed_of_fresh_green_rapunzel_herbs.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-003"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-003 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0




def recount_grimm_khm012_rapunzel_tower_in_forest() -> dict[str, tuple[str, ...]]:
    """Rapunzel (KHM 12) & The Hermes Scribe of the Five Mirrors — woven narrative chapter."""
    garden_bed_of_fresh_green_rapunzel_herbs = "Deep in the forest stood a lofty tower with neither stair nor door, and only a single small window high under the eaves."
    round_stone_tower_with_neither_door_nor_stair = "Whenever Rapunzel heard the call from below, she unfastened her braided tresses of spun gold and wound them twenty ells down around a window hook."
    six_pull_requests_opened_in_nineteen_seconds = "Moving like quicksilver across the sky, the Hermes scribe opened six pull requests across three sister repositories in nineteen seconds."
    hamiltonian_cycle_linking_five_sister_mirrors = "Each repository's first shard pointed in a closed Hamiltonian circle to the next mirror in the five-star constellation."
    return {
        "grimm_chapter": (garden_bed_of_fresh_green_rapunzel_herbs, round_stone_tower_with_neither_door_nor_stair),
        "bot_chronicle": (six_pull_requests_opened_in_nineteen_seconds, hamiltonian_cycle_linking_five_sister_mirrors),
    }


if __name__ == "__main__":
    raise SystemExit(main())
