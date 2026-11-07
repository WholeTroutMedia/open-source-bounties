# Free 3D Mesh, CAD & Media Cryptographic Watermarker (`watermark_asset_shield.py`)

**Invisible mathematical ownership proof for 3D models (`.obj`, `.gltf`), CAD files, and public media assets against unauthorized AI scraper training.**

## How It Works
- Computes an `HMAC-SHA256` signature from the creator's identity and embeds microscopic (`1e-6`) deterministic vertex coordinate parity into `.obj` / `.gltf` 3D geometry as well as RFC-compliant provenance metadata.
- Invisible to the human eye and 3D renderers, but preserved if an AI scraper or 3D asset farm copies your mesh.

## Usage
```bash
python3 watermark_asset_shield.py --sign model.obj --owner "WholeTroutMedia"
python3 watermark_asset_shield.py --verify model.obj --owner "WholeTroutMedia"
```
