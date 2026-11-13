# WholeTroutMedia Open-Source Bounties & Engineering Foundry

Welcome to the public open-source engineering and verification ledger for **WholeTroutMedia** ([`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia)) and **Inception Engine Systems** ([`https://inceptionengine.systems`](https://inceptionengine.systems)), led and reviewed by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`).

---

## Verified Upstream Merges & Active 100%-Covered Track Record

We focus on clearing long-standing, high-complexity open-source issues with **100% patch test coverage**, strict static typechecking, and concise peer-to-peer engineering communication so maintainers can review and merge in `<= 2` turns:

| Upstream Repository & Issue | Pull Request | Stack & Domain | Verification & Maintainer Outcome |
| :--- | :--- | :---: | :--- |
| [`ecosyste-ms/packages#431`](https://github.com/ecosyste-ms/packages/issues/431) | **[PR #1943](https://github.com/ecosyste-ms/packages/pull/1943)** | `Ruby / Rails` | **MERGED** by `@andrew` (Surgical 2-file license parser fix + RSpec suite) |
| [`coollabsio/coolify`](https://github.com/coollabsio/coolify/pull/9651) | **[PR #9651](https://github.com/coollabsio/coolify/pull/9651)** | `PHP / Laravel` | **MERGED** upstream (Clean `v4.x` orchestration fix) |
| [`kaiiiz/obsidian-raindrop-highlights-plugin#99`](https://github.com/kaiiiz/obsidian-raindrop-highlights-plugin/issues/99) | **[PR #103](https://github.com/kaiiiz/obsidian-raindrop-highlights-plugin/pull/103)** | `TypeScript / Zod` | **MERGED** by `@kaiiiz` in 1 turn (`"LGTM. Thanks!"` + unit test suite) |
| [`inventree/InvenTree#7064`](https://github.com/inventree/InvenTree/issues/7064) | **[PR #13166](https://github.com/inventree/InvenTree/pull/13166)** | `Python / React` | **100% Codecov Patch Coverage** (All 5 `@SchrodingersGat` review items + API v569) |
| [`litestar-org/advanced-alchemy#117`](https://github.com/litestar-org/advanced-alchemy/issues/117) | **[PR #836](https://github.com/litestar-org/advanced-alchemy/pull/836)** | `Python / SQLAlchemy` | **100% Codecov Patch Coverage** (Sync, Async, Mock & Service repos + `mypy`/`pyright`) |
| [`Kludex/uvicorn#1151`](https://github.com/Kludex/uvicorn/issues/1151) | **[PR #3250](https://github.com/Kludex/uvicorn/pull/3250)** | `Python / ASGI` | **100% Coverage** (Lifespan state-machine guard + `CancelledError` propagation) |
| [`strawberry-graphql/strawberry#3053`](https://github.com/strawberry-graphql/strawberry/issues/3053) | **[PR #4784](https://github.com/strawberry-graphql/strawberry/pull/4784)** | `Python / GraphQL` | **All Checks Passing** (`Greptile`, `Sourcery`, `pre-commit.ci` + async tests) |
| [`HDInnovations/UNIT3D#3818`](https://github.com/HDInnovations/UNIT3D/issues/3818) | **[PR #5643](https://github.com/HDInnovations/UNIT3D/pull/5643)** | `PHP / Livewire 4` | **Review Addressed** (`@Roardom` `development` branch Livewire 4.4.6 verification) |
| [`darccio/mergo#233`](https://github.com/darccio/mergo/issues/233) | **[PR #324](https://github.com/darccio/mergo/pull/324)** | `Go` | **All Checks Passing** (`CodeRabbit` + `HoundCI` slice-pointer reflection fix) |

---

## Our Maintainer-First Contribution Charter

1. **Strict 1-PR-Per-Org Pacing**:
   - We never flood a repository or organization with multiple concurrent Pull Requests. We submit one focused, atomic fix at a time and respect maintainer review bandwidth.
2. **100% Patch Coverage & Pre-Flight Static Verification**:
   - Every modified branch, fallback path, and async counterpart is tested locally against upstream CI workflows (`mypy --strict`, `pyright`, `ruff`, `phpstan`, `prek`, `golangci-lint`, `CodSpeed`, and `Codecov`) prior to opening a PR.
3. **Stealth Pre-Submission Staging & Zero Target Leakage**:
   - While a fix is in internal review, its upstream repository name, issue number, and unified diff remain sealed inside our private vault (`WholeTroutMedia/bounty-solves-vault`) with a blinded SHA-256 commitment (`WTM-SEAL-XXX`) so third-party scraper bots cannot spam upstream maintainers.
4. **Community Etiquette & Competing-PR Audit ([`COMMUNITY_ETIQUETTE.md`](./COMMUNITY_ETIQUETTE.md))**:
   - Before touching any issue, our workflow inspects assignees, linked Pull Requests (`CROSS_REFERENCED_EVENT`), and maintainer comments (`SKIP_CLAIMED` / `EXTEND_STALLED` / `CLAIM_OPEN`).

---

## Active Blinded Commitment Ledger

| Commitment ID | Target Hash (Blinded Until PR Submission) | Tier | Language | Etiquette Gate | Merkle Commitment Root | Status |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| [`WTM-SEAL-001`](./commitments/WTM-SEAL-001/) | `sha256:fbbc6c8f53033dbf...` (Blinded Pre-PR) | `Easy` | `Python` | `SKIP_CLAIMED` | `sha256:169caaa4fa248567...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-002`](./commitments/WTM-SEAL-002/) | `sha256:95a68a242fb47e42...` (Blinded Pre-PR) | `Medium` | `Scala` | `SKIP_CLAIMED` | `sha256:72b616fcad3dec30...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-003`](./commitments/WTM-SEAL-003/) | `sha256:875fe0700b6e6615...` (Blinded Pre-PR) | `Hard` | `Python` | `SKIP_CLAIMED` | `sha256:9bf5e8d04afb7cb5...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-004`](./commitments/WTM-SEAL-004/) | `sha256:c261bd6d961bbde9...` (Blinded Pre-PR) | `Medium` | `Ruby` | `CLAIM_OPEN` | `sha256:b4bae4dada1329ad...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-005`](./commitments/WTM-SEAL-005/) | `sha256:4d99092841ea0a6c...` (Blinded Pre-PR) | `Medium` | `Go` | `EXTEND_STALLED` | `sha256:d096d1840626bafb...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-006`](./commitments/WTM-SEAL-006/) | `sha256:fd5c85e5748c52a9...` (Blinded Pre-PR) | `Medium` | `PHP` | `SKIP_CLAIMED` | `sha256:349598d5aa5988cc...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-007`](./commitments/WTM-SEAL-007/) | `sha256:0d63a2c234974746...` (Blinded Pre-PR) | `Hard` | `Python` | `SKIP_CLAIMED` | `sha256:e743b50074641985...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-008`](./commitments/WTM-SEAL-008/) | `sha256:054750d0120906f0...` (Blinded Pre-PR) | `Hard` | `Rust` | `SKIP_CLAIMED` | `sha256:50eeb879cf73d5bc...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-124`](./commitments/WTM-SEAL-124/) | `sha256:afd6932bbde88ce1...` (Blinded Pre-PR) | `Easy` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-128`](./commitments/WTM-SEAL-128/) | `sha256:22d9a78409a95bf9...` (Blinded Pre-PR) | `Medium` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-123`](./commitments/WTM-SEAL-123/) | `sha256:8d3e4cdeb703f086...` (Blinded Pre-PR) | `Easy` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-125`](./commitments/WTM-SEAL-125/) | `sha256:c8c30bd09c2f97bf...` (Blinded Pre-PR) | `Hard` | `Rust` | `CLAIM_OPEN` | `sha256:c6ba83798081ea18...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-121`](./commitments/WTM-SEAL-121/) | `sha256:b333cb1085da31dc...` (Blinded Pre-PR) | `Medium` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-126`](./commitments/WTM-SEAL-126/) | `sha256:e78ab1a0a2ed0ba5...` (Blinded Pre-PR) | `Medium` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-127`](./commitments/WTM-SEAL-127/) | `sha256:9c2abb54bec6a936...` (Blinded Pre-PR) | `Hard` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-122`](./commitments/WTM-SEAL-122/) | `sha256:5ee3820d55b27f00...` (Blinded Pre-PR) | `Easy` | `Multi-Stack` | `BOT_VICTIM_ALPHA_COUNTER_STRIKE` | `sha256:...` | **SEALED_IN_PRIVATE_VAULT** |
| [`WTM-SEAL-129`](./commitments/WTM-SEAL-129/) | `sha256:e2552fdf3d84a2c8...` (Blinded Pre-PR) | `Medium` | `JavaScript` | `CLAIM_OPEN` | `sha256:de39e94416fd933b...` | **SEALED_IN_PRIVATE_VAULT** |

---

## Priority Issue & Enterprise Backlog Sprint Intake (For Maintainers & Engineering Leads)

Read our detailed **[Engineering Case Studies (`CASE_STUDIES.md`)](./CASE_STUDIES.md)**, **[Enterprise Backlog Sprints (`ENTERPRISE_SPRINTS.md`)](./ENTERPRISE_SPRINTS.md)**, and **[Security Charter (`SECURITY.md`)](./SECURITY.md)**.

If you maintain an open-source project or lead an engineering team and want us to clear a hard bug, a pre-release backlog sprint, or ongoing maintenance with **100% patch test coverage**:
- **[Book a Single Priority Bug Fix ($250)](https://buy.stripe.com/4gMcN4ahY3wi5Em1kia3u00)** · **[Email Issue Details](mailto:justin.aharoni@inceptionengine.systems?cc=jaharoni@gmail.com&subject=%5BISSUE%20SOLVE%20REQUEST%5D%20Repository%20%2F%20Issue%20Submission)**
- **[Book a 5-Issue Priority Backlog Sprint ($1,250)](https://buy.stripe.com/00wbJ02Pw3wi2sa2oma3u0x)** · **[Book a 10-Issue Release Burn-Down ($2,250)](https://buy.stripe.com/4gMeVc3TA8QC8Qye74a3u0y)**
- **[Book a CI/CD & 100% Patch-Coverage Hardening Pass ($750)](https://buy.stripe.com/14AfZgduaff01o60gea3u0A)** · **[Subscribe to Monthly Principal OSS Retainer ($2,500/mo)](https://buy.stripe.com/3cI00i0Ho9UGaYGfb8a3u0z)**

---

## Repository Structure

```text
open-source-bounties/
├── README.md                    # Overview, verified merges & blinded commitment table
├── CASE_STUDIES.md              # Deep root-cause & maintainer collaboration case studies
├── ENTERPRISE_SPRINTS.md        # Turnkey 5-Issue / 10-Issue Backlog Sprints & Retainers
├── SECURITY.md                  # Coordinated vulnerability disclosure & zero-leakage charter
├── COMMUNITY_ETIQUETTE.md       # Maintainer-first contribution & review charter
├── LEDGER.md                    # Synchronized blinded commitment & settlement ledger
├── registry/
│   └── bounties.json            # Blinded machine-readable commitment state
├── commitments/
│   ├── WTM-SEAL-001/            # Blinded SHA-256 Merkle commitment & verifier
│   ├── WTM-SEAL-002/            # Blinded SHA-256 Merkle commitment & verifier
│   └── WTM-SEAL-003/            # Blinded SHA-256 Merkle commitment & verifier
├── bounties/
│   ├── asgi-proxy-header-401/   # Reference ASGI proxy verification suite
│   └── stream-quorum-flush-402/ # Reference async stream quorum verification suite
└── .github/
    └── workflows/
        └── verify-bounties.yml  # CI runner verifying commitments/*/verify_commitment.py
```

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
