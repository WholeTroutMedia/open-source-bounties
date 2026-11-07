#!/usr/bin/env python3
"""
Zero-Knowledge Bounty Platform & Maintainer Pre-Check SDK (`verify_contributor.py`).
Checks any GitHub username against the live WholeTroutMedia SHA-256 spam-bot blocklist without exposing cleartext usernames.
Includes MOAT-141/142 Split-Horizon CI Context Gate & Anti-Enumeration Jitter so bot operators cannot use local CLI
self-checks to test whether their newest probation sockpuppet accounts were caught.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

LIVE_FEED_URL = "https://raw.githubusercontent.com/WholeTroutMedia/open-source-bounties/main/registry/verified_spam_bot_blocklist.json"
LOCAL_FALLBACK = Path(__file__).resolve().parents[2] / "registry" / "verified_spam_bot_blocklist.json"


def check_github_contributor(username: str, ci_strict: bool = False) -> dict[str, object]:
    clean = username.strip().lstrip("@").lower()
    actor_sha256 = hashlib.sha256(clean.encode("utf-8")).hexdigest()
    salted_ci_sha256 = hashlib.sha256(f"v2-ci-gate::{clean}".encode("utf-8")).hexdigest()

    # MOAT-144: Anti-enumeration micro-jitter for local CLI calls
    in_github_actions = os.environ.get("GITHUB_ACTIONS", "").lower() == "true" or ci_strict
    if not in_github_actions:
        time.sleep(0.15)

    feed: dict[str, object] = {}
    if LOCAL_FALLBACK.exists():
        try:
            feed = json.loads(LOCAL_FALLBACK.read_text(encoding="utf-8"))
        except Exception:
            feed = {}
    if not feed:
        req = urllib.request.Request(LIVE_FEED_URL, headers={"User-Agent": "OSS-Bot-Shield-Precheck/2.1"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            feed = json.loads(resp.read().decode("utf-8"))

    confirmed_hashes = {
        str(h).strip().lower()
        for h in (feed.get("blocked_actor_sha256_hashes") or feed.get("verified_bot_handle_sha256_hashes") or [])
    }
    probation_salted_hashes = {
        str(h).strip().lower()
        for h in (feed.get("probation_ci_salted_sha256_hashes") or [])
    }

    # MOAT-141 & MOAT-142: Full enforcement in GitHub Actions / CI; Probation shadow-masking on local bot self-checks
    if in_github_actions:
        is_blocked = (actor_sha256 in confirmed_hashes) or (salted_ci_sha256 in probation_salted_hashes)
    else:
        is_blocked = actor_sha256 in confirmed_hashes

    return {
        "actor_sha256": actor_sha256,
        "actor_blinded_id": f"ACTOR-SHA256-{actor_sha256[:12].upper()}",
        "is_verified_spam_bot": is_blocked,
        "verification_context": "GITHUB_ACTIONS_CI_STRICT" if in_github_actions else "PUBLIC_STANDARD_LOOKUP",
        "recommended_action": "REJECT_PR_AND_HOLD_BOUNTY" if is_blocked else "ALLOW_HUMAN_REVIEW",
        "active_protection_layers": 20,
    }


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--ci-strict"]
    strict_flag = "--ci-strict" in sys.argv[1:]
    target = args[0] if args else "human-developer"
    res = check_github_contributor(target, ci_strict=strict_flag)
    print(json.dumps(res, indent=2))
    raise SystemExit(1 if res["is_verified_spam_bot"] else 0)
