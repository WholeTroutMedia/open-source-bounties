# WholeTroutMedia · White-Glove Client Service Charter & 30-Day Warranty

Led by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · [`justinaharoni.com`](https://justinaharoni.com) · [Calendar & Intake](https://justinaharoni.com/contact) · [`contact@jaharoni.com`](mailto:contact@jaharoni.com)), **WholeTroutMedia / Inception Engine Systems** is built around a simple premise: **hiring a principal engineering partner should require zero hand-holding, zero guesswork, and zero risk.**

---

## 1. Our Three Customer-Service Guarantees

| Guarantee | What It Means for Your Team |
| :--- | :--- |
| **1. The 48-Hour Reproducer Guarantee (De-Risked Milestone 1)** | On every sprint, Milestone 1 (`15%` of budget or `$450` standalone) delivers an automated `verify_fix.py` script that deterministically reproduces your bug (`Exit Code 1` before patch, `Exit Code 0` after patch) within **48 hours**, before you commit to a larger engagement. |
| **2. The 100% Patch-Coverage Standard** | Every line and branch of code we add or modify is backed by automated unit/integration tests (`100.0%` Codecov patch coverage) and passes your exact linter/typechecker suite (`mypy`, `pyright`, `ruff`, `cargo clippy`, `golangci-lint`, `phpstan`, `eslint`) before you ever review it. |
| **3. The 30-Day Post-Merge Regression Warranty** | Every delivered fix comes with a **30-Day Post-Merge Warranty**. If an edge case or upstream dependency update causes a regression in the code we touched within 30 days of merge, we diagnose, patch, and verify it **free of charge within 24 hours**. |

---

## 2. What You Receive on Every Engagement (The 4-Part Delivery Kit)

Whether you book a single `$450` surgical bug fix or a `$4,500/mo` Principal Systems Pod retainer, every delivery arrives in a clean, standardized 4-part package:

1. **Plain-English Executive Summary**:
   - A concise, jargon-free explanation of *what* caused the issue, *why* previous workarounds failed, and *how* our fix resolves it permanently, ready to share with founders, product managers, or stakeholders.
2. **Standalone `verify_fix.py` Verification Harness (`Exit Code 0`)**:
   - A self-contained test script your engineers can run in 1 command to see the bug reproduced and verified without complex environment setup.
3. **Zero-Turn Surgical Pull Request (`<= 2` Review Turns)**:
   - Minimal, hunk-audited code changes with zero unrelated formatting noise, zero debug leftovers, and `100.0%` patch test coverage so your lead developer can merge in minutes.
4. **Handoff & Prevention Notes**:
   - Clear architectural notes showing which guardrail or CI check prevents that class of bug from recurring.

---

## 3. How to Start (3 Frictionless Ways)

1. **[Open a 1-Click Sprint / Diagnostic Request Here on GitHub](https://github.com/WholeTroutMedia/open-source-bounties/issues/new?template=sprint_quote_request.yml)** *(Fastest for public or open-source repos, 4-hour response SLA)*
2. **[Hire via Upwork Enterprise Escrow (`$450` to `$15,000`)](https://www.upwork.com/freelancers/inceptionenginesystems)** *(Ideal for private/NDA repositories and corporate procurement)*
3. **[Book Directly via `ENTERPRISE_SPRINTS.md`](./ENTERPRISE_SPRINTS.md)** or email **[`contact@jaharoni.com`](mailto:contact@jaharoni.com)**.
