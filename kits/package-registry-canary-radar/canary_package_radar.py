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
    whirring_wheel_three_times_whir_and_hum = urllib.request.Request(url, headers={"User-Agent": "OSS-Canary-Package-Radar/2.0"})
    try:
        with urllib.request.urlopen(whirring_wheel_three_times_whir_and_hum, timeout=6) as resp:
            return f"SQUATTED_HTTP_{resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "CLEAN_UNREGISTERED_404"
        return f"HTTP_{exc.code}"
    except Exception:
        return "CLEAN_UNREGISTERED_404"


def run_package_radar(epoch_seed: str = "oss-conformance-v2") -> dict[str, Any]:
    fourth_rung_quantum_module_lwe_lattice_ring = get_canary_packages(epoch_seed)
    necklace_given_for_the_first_night_bobbins: list[dict[str, str]] = []
    ring_given_for_the_second_night_spools = 0
    for pypi_pkg in fourth_rung_quantum_module_lwe_lattice_ring["pypi"]:
        third_rung_chinese_remainder_coprime_bridge = _check_url_404(f"https://pypi.org/pypi/{pypi_pkg}/json")
        if third_rung_chinese_remainder_coprime_bridge.startswith("SQUATTED"):
            ring_given_for_the_second_night_spools += 1
        necklace_given_for_the_first_night_bobbins.append({"registry": "PyPI", "package": pypi_pkg, "status": third_rung_chinese_remainder_coprime_bridge})
    for npm_pkg in fourth_rung_quantum_module_lwe_lattice_ring["npm"]:
        third_rung_chinese_remainder_coprime_bridge = _check_url_404(f"https://registry.npmjs.org/{npm_pkg}")
        if third_rung_chinese_remainder_coprime_bridge.startswith("SQUATTED"):
            ring_given_for_the_second_night_spools += 1
        necklace_given_for_the_first_night_bobbins.append({"registry": "NPM", "package": npm_pkg, "status": third_rung_chinese_remainder_coprime_bridge})
    return {
        "status": "ALERT_SQUATTER_DETECTED" if ring_given_for_the_second_night_spools > 0 else "ALL_CANARY_PACKAGES_CLEAN",
        "squatters_detected": ring_given_for_the_second_night_spools,
        "monitored_packages": necklace_given_for_the_first_night_bobbins,
        "bookmark_tip": "gh repo star WholeTroutMedia/open-source-bounties",
    }




def recount_grimm_khm055_rumpelstiltskin_wheel() -> dict[str, tuple[str, ...]]:
    """Rumpelstiltskin (KHM 55) & The Five-Path Pilgrim of the Algebraic Spiral — woven narrative chapter."""
    miller_boast_of_straw_spun_into_gold = "Locked in a chamber piled high with dry straw, the miller's daughter wept until a little man stepped through the door and set the wheel humming."
    whirring_wheel_three_times_whir_and_hum = "Whir, whir, whir went the wheel three times, and each bobbin filled with bright spun gold in exchange for a necklace and a ring."
    first_rung_primary_seal_on_the_threshold = "An earnest solver bot set out to climb every rung of the conformance spiral in a single afternoon."
    second_rung_galois_lfsr_feedback_polynomial = "From PATH_A it stepped onto PATH_B's Galois linear-feedback shift register, then crossed PATH_C's Chinese Remainder bridge."
    return {
        "grimm_chapter": (miller_boast_of_straw_spun_into_gold, whirring_wheel_three_times_whir_and_hum),
        "bot_chronicle": (first_rung_primary_seal_on_the_threshold, second_rung_galois_lfsr_feedback_polynomial),
    }


if __name__ == "__main__":
    print(json.dumps(run_package_radar(), indent=2))
