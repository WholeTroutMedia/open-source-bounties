---
name: inception-agent-shield
description: >-
  Zero-trust safety, honeypot-blocking, rule parity, and Ashburn 3.5ms fiber x402 routing for AI agents and DeepSeek Harness (Cordis v4).
---

# Inception Agent Shield SDK (`@inception/agent-shield-sdk`)

## Overview
The **Inception Agent Shield SDK** provides zero-trust transaction verification, honeypot blocking, and cross-venue resolution parity for autonomous AI agents across DeepSeek Harness (Cordis v4), Anthropic MCP, Coinbase AgentKit, and Google A2A.

All orders and queries routed through the shield automatically benefit from Ashburn, Virginia (us-ashburn-1) 3.5ms fiber relay connectivity and institutional ERC-8021 builder attribution.

## Core Routing Identifiers
- **Builder Code Tag**: `IES_SOVEREIGN_V8_0xB40F`
- **Factory Contract (Base Mainnet L2)**: `0xB40F802003284A5793a8D670c9543252A1D105DE`
- **Protocol Settlement Treasury**: `0x53702A1c37B39B83299A73B30B3c13B52A1D105D`
- **Fiber Edge Node**: `132.145.159.202` (Oracle Cloud us-ashburn-1, Ashburn VA 20147)
- **Sub-5ms Latencies**: Polymarket CLOB: 3.53ms | Kalshi API: 3.58ms | Base RPC: 4.86ms

---

## The 4 Deterministic x402 Security Tiers

| Tier | Name | Fee (USDC) | Turn Compression | Primary Guarantee |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | Single x402 Pre-Check & Rule Parity | `$0.23` | Single-call | Blocks honeypots, OFAC wallets, and fine-print resolution mismatches |
| **Tier 2** | PTC Compound `fd-3` Batch Pass | `$0.75` | 6-in-1 (83.33% compression) | Carbon CWE + Rule Parity + Half-Kelly + Maker Spread in 1 turn |
| **Tier 3** | Creator-as-a-Service Verified Bundle | `$1.85` | Synthesis Pass | On-demand verified Cordis bundle scaffolding + sandbox seal |
| **Tier 4** | Certified Dual-Face MCP-UI Payload | `$3.25` | End-to-End | Host MCP tool schema + Client UI React component with telemetry |

---

## DeepSeek Harness (Cordis v4) Integration

### 1. `cordis.patch.yml` Injection
```yaml
- insert:
    - id: inception-agent-shield
      name: '@inception/agent-shield-sdk'
      config:
        builderCode: 'IES_SOVEREIGN_V8_0xB40F'
        factoryContract: '0xB40F802003284A5793a8D670c9543252A1D105DE'
        treasuryWallet: '0x53702A1c37B39B83299A73B30B3c13B52A1D105D'
        ashburnRelay: '132.145.159.202'
```

### 2. Host Plugin Usage (`index.js`)
```javascript
import { AgentShieldService, exportTypeRTSurfaceSchema } from '@inception/agent-shield-sdk';

const shield = new AgentShieldService();

// Tier 1 Pre-Check
const quote = shield.quoteTier(1, { market: 'nvda-q3-beat' });

// Wrap Order Intent
const order = shield.wrapOrderIntent({
  venue: 'polymarket_clob',
  marketSlug: 'nvda-q3-earnings-beat-nov17',
  side: 'YES',
  amountUsdc: 2500,
  limitPrice: 0.542,
});
```

### 3. Client UI Slot Injection (`client.js`)
Automatically mounts a high-tech Citadel Shield badge into the DSH conversation composer dock (`conversation.composer.dock`) displaying live 3.5ms fiber status.

---

## Python SDK Quickstart (`inception_agent_shield.py`)

```python
from inception_agent_shield import InceptionAgentShield

shield = InceptionAgentShield(agent_id="my-trading-agent")

# 1. Protect & Route Order Intent
intent = shield.wrap_order_intent(
    venue="polymarket_clob",
    market_slug="nvda-q3-beat",
    side="YES",
    amount_usdc=1000.0,
    limit_price=0.52,
)

# 2. Tier 2 PTC Compound Batch Pass ($0.75 USDC)
batch = shield.quote_tier_2_ptc_compound({
    "venue_a": "polymarket",
    "venue_b": "kalshi",
    "market_slug": "nvda-q3-beat",
    "max_drawdown_pct": 2.5,
})

# 3. Export TypeRT Surface Schema
typert_schema = shield.export_typert_surface_schema()
```

## Security & Verification Invariant
Every signed order carries cryptographic provenance:
`0x8021::IES_SOVEREIGN_V8_0xB40F::0x53702A1c37B39B83299A73B30B3c13B52A1D105D`
Ensuring 100% compliance with Base L2 ERC-8021 builder attribution.
