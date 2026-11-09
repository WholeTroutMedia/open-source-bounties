# Kit #7: `stir-iescs-agent-protocol` (`STIR-1.0 + IESCS` Wire Protocol & Plain-English Receipt Kit)

Zero-dependency Python 3.9+ stdlib kit implementing:
- **STIR-1.0 (`Sovereign Ternary Inter-Agent Relay`)**: Strong Three-Valued Kleene Logic `{-1, 0, +1}` (`REJECT`, `HOLD_FOR_EVIDENCE`, `COMMIT`), Base-27 3-trit glyph encoding (`A-Z` + `_`), and Castagnoli CRC32C wire framing.
- **IESCS (`Prefix-Sigil Call-Words & Plain-English Receipt Compiler`)**: Compiles structured verification gates into compact `&domain:op{...}` call-words and automatically expands them into plain-English audit receipts for human maintainers.
- **Rosetta Handshake Header**: `X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`

## Quick Run
```bash
python3 kits/stir-iescs-agent-protocol/stir_iescs.py --json
```
