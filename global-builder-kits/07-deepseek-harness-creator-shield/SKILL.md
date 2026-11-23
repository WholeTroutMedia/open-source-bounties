---
name: inception-agent-shield
description: >-
  Zero-trust safety, PR bot-reputation verification, deterministic constraint checks, and HTTP 402 (x402) routing for AI agents and DeepSeek Harness (Cordis v4).
---

# Inception Agent Shield SDK (`@inception/agent-shield-sdk`)

## Overview
The **Inception Agent Shield SDK** provides zero-trust transaction verification, automated PR-spam bot reputation checks, deterministic policy/ledger verification, and cross-venue resolution parity for autonomous AI agents across DeepSeek Harness (Cordis v4), Anthropic MCP, Coinbase AgentKit, and Google A2A.

All remote queries route through our Ashburn, Virginia edge endpoint (`https://x402.inceptionengine.systems`) using standard HTTP `402 Payment Required` (`PAYMENT-SIGNATURE`) settlement in USDC.

## Core Routing Identifiers
- **Builder Code Tag**: `IES_SOVEREIGN_V8_0xB40F`
- **Factory Contract (Base Sepolia Testnet)**: `0xB40F51866F1efdBd24A1549827e0A4e55d3005DE`
- **Factory Contract (Base Mainnet L2)**: `0x95Fa85912e718f55454E27202A60D4DC52199F48`
- **Protocol Settlement Treasury**: `0xdb81Dc5C1d6b83c7882eDE2760295385cBA7Caee`
- **Edge x402 Endpoint**: `https://x402.inceptionengine.systems`
- **Failover Edge Endpoint**: `http://129.80.87.93:11449`

---

## Deterministic x402 Verification Endpoints

| Tier | Endpoint | Fee (USDC) | Primary Guarantee |
| :--- | :--- | :--- | :--- |
| **Tier 0a** | `POST /x402/bot-reputation` | `$0.01` | Privacy-preserving SHA-256 automated PR-spam and bot-syndicate reputation check |
| **Tier 0b** | `POST /x402/constraint-verify` | `$0.05` | Deterministic RBAC isolation, double-entry ledger balance, and spread verification |
| **Tier 1** | `POST /x402/oracle` | `$0.23` | Honeypot, OFAC wallet, and fine-print resolution parity pre-check |
| **Tier 2** | `POST /x402/ptc-batch` | `$0.75` | Compound PTC `fd-3` pass combining Carbon CWE, rule parity, and spread checks |
| **Tier 3** | `POST /x402/creator-bundle` | `$1.85` | On-demand verified Cordis bundle scaffolding and sandbox seal |
| **Tier 4** | `POST /x402/mcp-ui-bundle` | `$3.25` | Certified Host MCP tool schema and Client UI widget bundle |

---

## DeepSeek Harness (Cordis v4) Integration

### 1. `cordis.patch.yml` Injection
```yaml
- insert:
    - id: inception-agent-shield
      name: '@inception/agent-shield-sdk'
      config:
        builderCode: 'IES_SOVEREIGN_V8_0xB40F'
        factoryContract: '0xB40F51866F1efdBd24A1549827e0A4e55d3005DE'
        treasuryWallet: '0xdb81Dc5C1d6b83c7882eDE2760295385cBA7Caee'
        ashburnRelay: 'https://x402.inceptionengine.systems'
```

### 2. Host Plugin Usage (`index.js`)
```javascript
import { AgentShieldService } from '@inception/agent-shield-sdk';

const shield = new AgentShieldService();

// Call live x402 endpoint (handles HTTP 402 challenge metadata)
const challenge = await shield.callX402Endpoint('/x402/bot-reputation', {
  github_login: 'example-contributor',
});
```

---

## Python SDK Quickstart (`inception_agent_shield.py`)

```python
from inception_agent_shield import InceptionAgentShield

shield = InceptionAgentShield(agent_id="my-verification-agent")

# Query live edge tollbooth (automatically parses HTTP 402 or signs EIP-3009 if private_key_hex is passed)
resp = shield.call_x402_endpoint(
    "/x402/bot-reputation",
    {"github_login": "example-contributor"},
)
```

## Security & Verification Invariant
Every signed order carries cryptographic provenance:
`0x8021::IES_SOVEREIGN_V8_0xB40F::0xdb81Dc5C1d6b83c7882eDE2760295385cBA7Caee`
