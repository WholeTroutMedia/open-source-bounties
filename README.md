# WholeTroutMedia Open-Source Bounties & Engineering Foundry

Welcome to the public open-source engineering and verification ledger for **WholeTroutMedia** ([`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia)) and **Inception Engine Systems** ([`https://inceptionengine.systems`](https://inceptionengine.systems)), led and reviewed by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`).

---

## Stealth Pre-Submission Staging & Zero-Knowledge Commitments

1. **Zero Target Leakage Before PR Submission**:
   - While a fix is awaiting human review, its upstream repository name, issue number, unified diff (`patch.diff`), verification suite (`verify_fix.py`), and Pull Request draft (`PR_DRAFT.md`) live **exclusively inside our private vault** (`WholeTroutMedia/bounty-solves-vault`).
   - Only a blinded cryptographic commitment (`WTM-SEAL-XXX`) is published here prior to submission so automated third-party scrapers cannot harvest our active targets or spam upstream maintainers.
2. **Community Etiquette & Competing-PR Audit ([`COMMUNITY_ETIQUETTE.md`](./COMMUNITY_ETIQUETTE.md))**:
   - Before touching any issue, our workflow inspects assignees, linked Pull Requests (`CROSS_REFERENCED_EVENT`), and maintainer comments (`SKIP_CLAIMED` / `EXTEND_STALLED` / `CLAIM_OPEN`).
3. **Canary Decoy Benchmarks (`bounties/canary-trap-*`)**:
   - Synthetic canary directories under `bounties/canary-trap-*` contain watermarked decoy tokens (`_wtm_canary_*`) to fingerprint automated scrapers.

---

## Active Blinded Commitment Ledger

| Commitment ID | Target Hash (Blinded Until PR Submission) | Tier | Language | Etiquette Gate | Merkle Commitment Root | Status |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| [`WTM-SEAL-001`](./commitments/WTM-SEAL-001/) | `sha256:fbbc6c8f53033dbf...` (Blinded Pre-PR) | `Easy` | `Python` | `EXTEND_STALLED` | `sha256:f7978f99b1547881...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-002`](./commitments/WTM-SEAL-002/) | `sha256:95a68a242fb47e42...` (Blinded Pre-PR) | `Medium` | `Scala` | `EXTEND_STALLED` | `sha256:cecf0404374f0abf...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-003`](./commitments/WTM-SEAL-003/) | `sha256:875fe0700b6e6615...` (Blinded Pre-PR) | `Hard` | `Python` | `EXTEND_STALLED` | `sha256:5ef793080d51f576...` | **SEALED_IN_PRIVATE_VAULT** |

---

## Have an Issue or Repository You Want Solved?

If you maintain an open-source project and have a bug or bounty you would like our system to solve, verify (`Exit Code 0`), and stage for review:
- **[Request a Verified Fix (`justin.aharoni@inceptionengine.systems`)](mailto:justin.aharoni@inceptionengine.systems?cc=jaharoni@gmail.com&subject=%5BISSUE%20SOLVE%20REQUEST%5D%20Repository%20%2F%20Issue%20Submission&body=Hi%20Justin%2C%0A%0AWe%20would%20like%20WholeTroutMedia%20to%20look%20at%20and%20verify%20a%20fix%20for%3A%0A-%20Repository%3A%20%0A-%20Issue%3A%20%0A-%20Notes%3A%20%0A%0AThank%20you!)**

---

## Repository Structure

```text
open-source-bounties/
├── README.md                    # Overview & blinded commitment table
├── COMMUNITY_ETIQUETTE.md       # Maintainer-first contribution & review charter
├── LEDGER.md                    # Synchronized blinded commitment & settlement ledger
├── registry/
│   └── bounties.json            # Blinded machine-readable commitment state
├── commitments/
│   ├── WTM-SEAL-001/            # Blinded SHA-256 Merkle commitment & verifier
│   ├── WTM-SEAL-002/            # Blinded SHA-256 Merkle commitment & verifier
│   └── WTM-SEAL-003/            # Blinded SHA-256 Merkle commitment & verifier
├── bounties/
│   ├── canary-trap-01-.../      # Synthetic watermarked canary decoy for scrapers
│   └── canary-trap-02-.../      # Synthetic watermarked canary decoy for scrapers
└── .github/
    └── workflows/
        └── verify-bounties.yml  # CI runner verifying commitments/*/verify_commitment.py
```

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
