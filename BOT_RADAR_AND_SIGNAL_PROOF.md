# WholeTroutMedia 6-Beacon Counter-Bot Radar & Signal Proof

*Last synchronized: 2026-10-26 15:07 UTC*

Open-source maintainers today are inundated by automated scraper bots that poll GitHub for the word `"bounty"`, dump raw issue text into a single-shot prompt wrapper, and paste 200 lines of unverified prose without ever cloning the repository or running a single test.

To make sure **WholeTroutMedia** never falls into bot traps, never adds to maintainer noise, and delivers undeniable engineering value, we operate a **6-Beacon Counter-Bot Constellation** that monitors known scraper accounts across GitHub's public event stream (`/users/{actor}/events/public`).

---

## 1. Live 6-Beacon Counter-Bot Constellation (`registry/bot_intelligence.json`)

| Tracked Bot Beacon | Bot Velocity Score | Forensic Construction & Indicators | Recent Repositories Targeted by Bot |
| :--- | :---: | :--- | :--- |
| **Beacon #1**: `@fangjian-bit` | `100/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (UnsafeLabs/Bounty-Hunters, relayhop/sn-monetization-runtime)<br/>High cross-repo comment velocity (28 comments across 14 repos)<br/>Zero code PushEvents/PullRequestEvents despite cross-repo issue commenting<br/>Hardcoded Expensify/Upwork LLM prompt template detected (12 hits) | `Expensify/App`, `UnsafeLabs/Bounty-Hunters`, `auscaster/frantic-board`, `commonworld-one/commonworld`, `jadolg/elodin` |
| **Beacon #2**: `@Krusheek` | `80/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (Peter7896/TentOfTrials, UnsafeLabs/Bounty-Hunters, claude-builders-bounty/claude-builders-bounty, tine1117/oss-hunter-livefire)<br/>High cross-repo comment velocity (8 comments across 6 repos) | `Peter7896/TentOfTrials`, `UnsafeLabs/Bounty-Hunters`, `claude-builders-bounty/claude-builders-bounty`, `demetriodiazdeleon-pixel/morriganprueba`, `javelin-anticheat/py-workedtask` |
| **Beacon #3**: `@Madatest` | `80/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (alfrexo95/bounty-bot, amiller/bounty-arcade, relayhop/sn-monetization-runtime, zhangjiayang6835-cyber/bounty-plaza)<br/>High cross-repo comment velocity (17 comments across 9 repos) | `BasedHardware/omi`, `SPLURT-Station/S.P.L.U.R.T-tg`, `alfrexo95/bounty-bot`, `amiller/bounty-arcade`, `dsect-net/quantum` |
| **Beacon #4**: `@Jah-yee` | `80/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (darpansanghani/swe-agent-playground)<br/>High cross-repo comment velocity (18 comments across 18 repos) | `AdobeDocs/substance-3d-painter.en`, `Dorset-Council-UK/QGIS.Mosaic.Builder`, `Garados007/MaxLib.WebServer`, `KenyC/LingExRef`, `bugcrowd/HUNT` |
| **Beacon #5**: `@livastic-vm1-primary` | `40/100` (`SUSPICIOUS_SCRAPER`) | High cross-repo comment velocity (11 comments across 8 repos) | `causeway-services/.github`, `conclave-admin/conclave-main`, `dancaldera/creativelab`, `diogel-io/bancwr`, `fanout-web/fanout-contracts` |
| **Beacon #6**: `@aiautomationagentesting` | `80/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (Circadian-agent/agent-collective)<br/>High cross-repo comment velocity (10 comments across 6 repos) | `Circadian-agent/agent-collective`, `OpsiMate/OpsiMate`, `X-lab2017/open-dipper`, `kanghyunsoon/duo`, `marcellosso/penciled` |
| **Beacon #7**: `@BP202302` | `80/100` (`AUTOMATED_SLOP_BOT`) | Triggered known honeypot/bot-bait traps (SecureBananaLabs/bug-bounty, claude-builders-bounty/claude-builders-bounty)<br/>High cross-repo comment velocity (6 comments across 4 repos) | `SecureBananaLabs/bug-bounty`, `auscaster/frantic-board`, `claude-builders-bounty/claude-builders-bounty`, `illbnm/homelab-stack` |

---

## 2. Multi-Beacon Overlap: Confirmed Bot Traps We Explicitly Avoid

When two or more tracked scraper beacons converge on the same repository, our **5-Gate Community Etiquette & Anti-Honeypot Filter** automatically blocks or flags the target so we never waste engineering cycles on synthetic bot traps:

| Convergent Repository Target | Overlapping Beacons Detected | WholeTroutMedia Disposition |
| :--- | :--- | :--- |
| `UnsafeLabs/Bounty-Hunters` | `2 Beacons` (`@fangjian-bit`, `@Krusheek`) | **BLOCKED HONEYPOT / BOT TRAP (Never Touch)** |
| `auscaster/frantic-board` | `2 Beacons` (`@fangjian-bit`, `@BP202302`) | **BOT-SPAMMED REPO (Requires Extra Maintainer Care)** |
| `claude-builders-bounty/claude-builders-bounty` | `2 Beacons` (`@Krusheek`, `@BP202302`) | **BLOCKED HONEYPOT / BOT TRAP (Never Touch)** |
| `limitlessprojects/Go-Hybrid` | `2 Beacons` (`@fangjian-bit`, `@livastic-vm1-primary`) | **BOT-SPAMMED REPO (Requires Extra Maintainer Care)** |
| `relayhop/sn-monetization-runtime` | `2 Beacons` (`@fangjian-bit`, `@Madatest`) | **BLOCKED HONEYPOT / BOT TRAP (Never Touch)** |

---

## 3. Signal vs. Slop: How We Prove Authentic Engineering Value

| Verification Dimension | Automated Scraper Bots (`@fangjian-bit`, `@Krusheek`, etc.) | **WholeTroutMedia Engineering Foundry** |
| :--- | :--- | :--- |
| **Human Provenance & Accountability** | Anonymous burner accounts (`0` followers, automated Upwork/Expensify templates) | Reviewed and signed off by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`) |
| **Competing-PR Etiquette** | Blindly spams issues that already have open PRs or assignees | Queries GraphQL `CROSS_REFERENCED_EVENT` timelines; skips active PRs (`SKIP_CLAIMED`) and credits prior stalled contributors (`EXTEND_STALLED`) |
| **Code Execution Proof** | `0` commits, `0` pushes, `0` tests executed | Every dossier includes a standalone `verify_fix.py` reproduction harness exiting `0` in `<30 ms` + SHA-256 [`PROOF_OF_EXECUTION.md`](./bounties/starlette-843/PROOF_OF_EXECUTION.md) |
| **Clean Organization Fork** | None (pastes uncompiled code blocks into issue comments) | Clean branch pushed to `https://github.com/WholeTroutMedia/<repo>` |


---
**Human Review & Provenance**
- **Reviewed & Approved By**: Justin Aharoni ([@jaharoni](https://github.com/jaharoni))
- **Direct Contact**: `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`
- **Engineering Studio**: [WholeTroutMedia](https://github.com/WholeTroutMedia) / [Inception Engine Systems](https://inceptionengine.systems)
- **Verification & Counter-Bot Ledger**: [WholeTroutMedia/open-source-bounties](https://github.com/WholeTroutMedia/open-source-bounties)

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
