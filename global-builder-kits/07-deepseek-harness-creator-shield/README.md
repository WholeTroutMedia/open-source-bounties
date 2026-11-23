# DeepSeek Harness Creator Shield & 4-Tier x402 Routing Kit (`07-deepseek-harness-creator-shield`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: DeepSeek Harness (`dsh` / Cordis v4), Anthropic MCP, Coinbase AgentKit, and Google A2A Agent Builders Worldwide
> - **Stack**: `Python 3.10+, Node.js ES Modules (Cordis v4 & TypeRT), YAML`
> - **Static Plugin Market Index**: [`registry/dsh_plugin_market.index.json`](../../registry/dsh_plugin_market.index.json)
> - **Dependencies**: `0` (Standard Library Only)

## Why This Folder Exists

Autonomous trading and coding agents routinely lose execution edge to four failure modes: malicious or unverified tool inputs, upstream fork drift when tuning third-party plugins, truncated `SKILL.md` capability instructions above 8,192 characters, and high-latency multi-turn tool loops. This care package ships `@inception/agent-shield-sdk` v8.0.0 as a hot-loadable Cordis v4 `dsh-plugin` and Python SDK with monotonic `ctx.tools.guard` safety, zero-code `cordis.patch.yml` overrides, `TypeRT` runtime schema reflection, Ashburn 3.5ms fiber routing (`IES_SOVEREIGN_V8_0xB40F`), and 6-endpoint tiered `x402` USDC verification.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
python3 inception_agent_shield.py
```

## Verification Tiers

| Tier | Endpoint | Fee (USDC) | Primary Guarantee |
| :--- | :--- | :---: | :--- |
| **Tier 0a** | `POST /x402/bot-reputation` | `$0.01` | Privacy-preserving SHA-256 automated PR-spam and bot-syndicate reputation lookup |
| **Tier 0b** | `POST /x402/constraint-verify` | `$0.05` | Deterministic RBAC isolation, double-entry ledger balance, and cross-venue spread verification |
| **Tier 1** | `POST /x402/oracle` | `$0.23 - $0.35` | Honeypot, OFAC wallet, bio/regulatory wire, and resolution-clause parity pre-check |
| **Tier 2** | `POST /x402/ptc-batch` | `$0.75` | Compound `PTC` `fd-3` pass combining Carbon CWE, rule parity, sizing, spread, FOK, and `ERC-8021` rebate |
| **Tier 3** | `POST /x402/creator-bundle` | `$1.85` | On-demand verified Cordis v4 + MCP hot-bundle synthesis with `TypeRT` schema |
| **Tier 4** | `POST /x402/mcp-ui-bundle` | `$3.25` | Certified Host MCP contract + Browser `client.js` UI dock widget locked to zero-scroll safety |

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Zero-dependency verifier proving monotonic guard absorption, `cordis.patch.yml` idempotence, `PTC` compression, and `ERC-8021` rebate math.
- [`inception_agent_shield.py`](./inception_agent_shield.py): Drop-in Python SDK for MCP, A2A, AgentKit, LangGraph, and DeepSeek Harness agents.
- [`index.js`](./index.js) & [`client.js`](./client.js): Dual-face Cordis v4 ES-module host plugin (`ctx.tools.guard` + `TypeRT`) and browser composer dock badge.
- [`cordis.patch.yml`](./cordis.patch.yml) & [`package.json`](./package.json): Declarative Cordis v4 bundle configuration (`dsh >= 0.2.0-rc.2`).
- [`SKILL.md`](./SKILL.md) & [`plugin-market.index.json`](./plugin-market.index.json): Pruner-safe (`<8,192` chars) skill descriptor and static plugin market manifest.
