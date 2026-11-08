# WholeTroutMedia Open-Source Contribution & Etiquette Charter

This repository (`WholeTroutMedia/open-source-bounties`) is our public engineering ledger for auditing, verifying, and staging open-source bug fixes and funded community bounties prior to submitting Pull Requests upstream.

Open-source maintainers spend enormous energy triaging issues and reviewing code. Our goal is to make every contribution from **WholeTroutMedia** a genuine relief to review: surgical, well-tested, respectful of existing contributors, and reviewed by a human before submission.

---

## 1. Competing-PR & Prior-Work Audit (`CLAIM_OPEN` / `EXTEND_STALLED` / `SKIP_CLAIMED`)

Before writing code or claiming an issue, our workflow inspects the upstream issue timeline, assignees, and linked Pull Requests:

1. **`SKIP_CLAIMED` (Respect Active Contributors)**:
   - If a maintainer has already assigned the issue to another developer, we skip it.
   - If another contributor already has an active, substantive open Pull Request addressing the issue, we skip it completely so we never duplicate active work.

2. **`EXTEND_STALLED` (Unify & Credit Prior Attempts)**:
   - When an issue has prior comments with debugging notes or an older Pull Request that stalled or closed without merging, we explicitly credit the earlier contributors (`@handle`) in our notes and build cleanly on their findings, while also reviewing prior CI check results so our patch resolves any remaining test edge cases.

3. **`CLAIM_OPEN` (Greenfield Unclaimed Target)**:
   - Zero assignees and zero active competing Pull Requests. We fork the repository into the **`WholeTroutMedia`** GitHub organization, reproduce the issue locally, and verify the fix before requesting review.

---

## 2. Clean Organization Isolation (`WholeTroutMedia` Only)

- All upstream forks created for bounty and bug-fix work live exclusively under the **`WholeTroutMedia`** GitHub organization (`https://github.com/WholeTroutMedia/<repo>`).
- While a fix is awaiting human review, the raw patch (`patch.diff`), standalone reproduction suite (`verify_fix.py`), and Pull Request draft (`PR_DRAFT.md`) are staged inside our private vault (our pre-release verification archive) and attested publicly via SHA-256 commitment (`solve_envelope.sealed.json`).

---

## 3. Verification First, Upstream PR Second (The Review Gate)

Nothing is submitted upstream automatically:

1. **Daily 08:45 AM Draft Cadence (`Easy -> Medium -> Hard`)**:
   - Each morning, our foundry selects one verified unclaimed issue along a rotating difficulty scale (`Easy`, `Medium`, `Hard`).
   - It validates the fix against a standalone reproduction and regression harness (`verify_fix.py`, which must exit `0`) and stages the full review package in our pre-release verification archive.
2. **Staged Human Review & Maintainer Fast-Track**:
   - The public commitment receipt is logged in [`LEDGER.md`](./LEDGER.md), opened as a tracking review issue in this repository, and emailed to Justin (`contact@jaharoni.com`) for review.
   - Verified maintainers of the upstream repository can request immediate PR submission or vault access at any time via the fast-track link in each dossier.
3. **Approved Upstream Submission**:
   - Once reviewed and approved, we push the topic branch (`fix/issue-<number>-<slug>`) to `WholeTroutMedia/<repo>` and open the Pull Request against the upstream repository.

---

## 4. Communication & Attribution Standard

- **Acknowledge the Maintainer First**: Every PR and issue comment opens by acknowledging the specific problem, reproduction steps, or design constraint the maintainer described.
- **Peer-to-Peer Engineering Prose**: We write in plain, friendly, peer-to-peer engineering prose with zero em-dashes and zero generic boilerplate.
- **Clear Human Accountability**: Every outbound contribution is personally reviewed and verified by **Justin Aharoni** (`@jaharoni`) prior to submission.

---

## 5. Maintainer Philosophical Buy-In & Alignment Gate

Passing automated CI checks is necessary but never sufficient if a core maintainer disagrees with an underlying feature request or specification extension. Before opening any Pull Request, our pre-flight gate classifies the upstream issue into one of three alignment tiers:

1. **`TIER_A_MAINTAINER_BLESSED`**:
   - The issue was opened by, labeled `help wanted` / `accepting PRs` by, or explicitly endorsed in comments by a repository `OWNER`, `MEMBER`, or `COLLABORATOR`. Eligible for immediate verification and PR submission.
2. **`TIER_B_CONFIRMED_BUG`**:
   - A deterministic, reproducible defect (crash, regression, race condition, memory leak, or type error) with a standalone `verify_fix.py` reproducer. Eligible for surgical bug-fix submission.
3. **`TIER_C_UNBLESSED_FEATURE_WISHLIST` (`HOLD_FOR_MAINTAINER_ALIGNMENT`)**:
   - An enhancement, new API argument, or specification extension requested by a community user without core-maintainer sign-off. We **hold** upstream PR submission and ask a concise architectural alignment question on the issue first so maintainers never face unsolicited feature PRs.

---

## 6. Global Ecosystem Stewardship, Junior Mentorship & Scoped Boundary

Solving complex bugs at global scale carries a responsibility to strengthen, rather than crowd out, the broader open-source ecosystem:

- **Protecting First-Timer & Junior Onboarding**: We do not snipe trivial `good first issue` / `first-timers-only` onboarding issues under 7 days old. Instead, when an onboarding issue has stalled for weeks, we publish educational root-cause walkthroughs so newer contributors learn the underlying systems mechanics.
- **Strict Review-Bandwidth Respect**: We enforce a hard cap of **1 active open PR per repository/organization** at any time so volunteer maintainers are never overwhelmed.
- **Scoped Solve Boundary**: We deliver complete, verified fixes for the specific issue in scope (plus our **30-Day Post-Merge Regression Warranty**), and route broader multi-issue roadmap or custom feature work to our structured [Wednesday 9:23 PM Community Tracker](./WEDNESDAY_923_COMMUNITY_TRACKER.md) or [Enterprise Backlog Sprints](./ENTERPRISE_SPRINTS.md).
