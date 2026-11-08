# Free PyPI & NPM Dependency-Confusion Early-Warning Radar (`canary_package_radar.py`)

**Catches malicious supply-chain bots that scan GitHub repositories for unpublished package names to register malware on PyPI (`pip`) or NPM (`npm`).**

## How It Works
1. Generates deterministic, unpublished canary package identifiers embedded inside conformance test manifests.
2. Queries `https://pypi.org/pypi/<pkg>/json` and `https://registry.npmjs.org/<pkg>` to verify `HTTP 404` (unpublished).
3. If any automated supply-chain bot registers a canary package name on PyPI or NPM, the radar immediately flags `SUPPLY_CHAIN_SQUATTER_DETECTED` so package registry security teams can quarantine the squatter before any developer downloads it.

## Usage
```bash
python3 canary_package_radar.py --check
```
