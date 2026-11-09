# Low-Resource Speech & TTS Dataset Validator (Kolokwa / Creole / Multilingual) (`04-kolokwa-low-resource-speech-evaluator`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: West African, MENA & Southeast Asian Voice AI Builders (@leinvoice on Kolokwa / Liberian English `lir` TTS, Arabic, Bahasa Indonesia & Thai AI builders)
> - **Stack**: `Python`
> - **Domain Hub**: [`by-domain/06-ai-studio-mcp-and-global-diagnostics`](../../by-domain/06-ai-studio-mcp-and-global-diagnostics/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Deterministic manifest auditor for low-resource TTS and ASR datasets: checks speaker leakage across train/eval splits, flags duration-to-character alignment anomalies, and normalizes creole/dialect orthography.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
