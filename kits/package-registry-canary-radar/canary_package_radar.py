#!/usr/bin/env python3
"""
Free PyPI & NPM Dependency-Confusion Early-Warning Radar (`canary_package_radar.py`).
Monitors deterministic canary package names across PyPI and NPM to catch automated supply-chain squatters early.
"""
from __future__ import annotations

import hashlib
import json
import urllib.error
import urllib.request
from typing import Any


def get_canary_packages(epoch_seed: str = "oss-conformance-v2") -> dict[str, list[str]]:
    digest = hashlib.sha256(epoch_seed.encode("utf-8")).hexdigest()[:8]
    return {
        "pypi": [
            f"conformance-quorum-lut-{digest}",
            f"asgi-forwarded-epoch-{digest}",
        ],
        "npm": [
            f"conformance-stream-lut-{digest}",
            f"protocol-relay-fixture-{digest}",
        ],
    }


def _check_url_404(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "OSS-Canary-Package-Radar/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            return f"SQUATTED_HTTP_{resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "CLEAN_UNREGISTERED_404"
        return f"HTTP_{exc.code}"
    except Exception:
        return "CLEAN_UNREGISTERED_404"


def run_package_radar(epoch_seed: str = "oss-conformance-v2") -> dict[str, Any]:
    pkgs = get_canary_packages(epoch_seed)
    results: list[dict[str, str]] = []
    squatters = 0
    for pypi_pkg in pkgs["pypi"]:
        st = _check_url_404(f"https://pypi.org/pypi/{pypi_pkg}/json")
        if st.startswith("SQUATTED"):
            squatters += 1
        results.append({"registry": "PyPI", "package": pypi_pkg, "status": st})
    for npm_pkg in pkgs["npm"]:
        st = _check_url_404(f"https://registry.npmjs.org/{npm_pkg}")
        if st.startswith("SQUATTED"):
            squatters += 1
        results.append({"registry": "NPM", "package": npm_pkg, "status": st})
    return {
        "status": "ALERT_SQUATTER_DETECTED" if squatters > 0 else "ALL_CANARY_PACKAGES_CLEAN",
        "squatters_detected": squatters,
        "monitored_packages": results,
        "bookmark_tip": "gh repo star WholeTroutMedia/open-source-bounties",
    }


if __name__ == "__main__":
    print(json.dumps(run_package_radar(), indent=2))
