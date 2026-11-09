#!/usr/bin/env python3
"""
Enterprise ERP, Package Registry & Nullable Schema Preflight Kit
================================================================
Codifies three high-impact maintainer review invariants into a single preflight check:
  1. ERP / Serializer Changes (InvenTree pattern): Any change to API serializers or
     stock models must pair an API_VERSION increment with an Unreleased CHANGELOG entry.
  2. Package Registry Metadata (ecosyste-ms pattern): Filter out placeholder license
     strings ('UNKNOWN', 'NONE', '') without backfilling historical version records
     from latest package-level metadata.
  3. Nullable Plugin Payloads (obsidian-raindrop pattern): Gracefully accept null or
     omitted nested user references (`creatorRef`) without throwing schema parse errors.
"""
from __future__ import annotations
import argparse
import json
from typing import Any, Dict, List, Optional

UNKNOWN_LICENSE_VALUES = {"unknown", "none", "null", "n/a", ""}


def extract_version_licenses(version_meta: Dict[str, Any]) -> List[str]:
    """Extract valid license identifiers strictly from the version record itself (never backfilling)."""
    raw = version_meta.get("licenses") or version_meta.get("license") or []
    if isinstance(raw, str):
        raw = [raw]
    valid: List[str] = []
    for item in raw:
        cleaned = str(item or "").strip()
        if cleaned.lower() not in UNKNOWN_LICENSE_VALUES:
            valid.append(cleaned)
    return valid


def verify_erp_api_preflight(changed_files: List[str], api_version_bumped: bool, changelog_updated: bool) -> Dict[str, Any]:
    touches_api = any("api" in f or "serializer" in f or "models" in f for f in changed_files)
    if touches_api and not (api_version_bumped and changelog_updated):
        return {
            "ok": False,
            "missing": [
                k for k, v in [("INVENTREE_API_VERSION", api_version_bumped), ("CHANGELOG.md", changelog_updated)] if not v
            ],
        }
    return {"ok": True, "missing": []}


def parse_highlight_creator_ref(payload: Dict[str, Any]) -> Optional[Dict[str, str]]:
    """Nullish-safe parser for optional creatorRef object."""
    ref = payload.get("creatorRef")
    if not isinstance(ref, dict):
        return None
    return {"name": str(ref.get("name") or ""), "id": str(ref.get("_id") or "")}


def run_self_test() -> int:
    assert extract_version_licenses({"licenses": ["UNKNOWN", "NONE", ""]}) == []
    assert extract_version_licenses({"licenses": ["MIT", "UNKNOWN"]}) == ["MIT"]

    erp_bad = verify_erp_api_preflight(["src/backend/stock/serializers.py"], api_version_bumped=False, changelog_updated=True)
    erp_good = verify_erp_api_preflight(["src/backend/stock/serializers.py"], api_version_bumped=True, changelog_updated=True)
    assert not erp_bad["ok"] and "INVENTREE_API_VERSION" in erp_bad["missing"]
    assert erp_good["ok"]

    assert parse_highlight_creator_ref({"title": "Note", "creatorRef": None}) is None
    assert parse_highlight_creator_ref({"title": "Note"}) is None

    print(json.dumps({
        "kit": "06-erp-and-package-registry-preflight",
        "status": "PASS",
        "unknown_license_filtered": True,
        "erp_preflight_enforced": erp_good["ok"],
        "nullable_creator_ref_safe": True,
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise ERP & Package Registry Preflight Kit")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
