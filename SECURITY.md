# Security & Coordinated Vulnerability Disclosure Charter (`SECURITY.md`)

**WholeTroutMedia / Inception Engine Systems** adheres to strict defensive security, supply-chain integrity, and zero-leakage disclosure practices across all open-source contributions and security audits.

---

## 1. Zero Target Leakage & Blinded Pre-Submission Vault
- Any security-sensitive bug, memory corruption fix, or supply-chain hardening patch is developed and verified exclusively inside our private vault (`WholeTroutMedia/bounty-solves-vault`).
- Public commitment tables in this repository publish only salted SHA-256 Merkle commitments (`WTM-SEAL-XXX`) prior to maintainer coordination so third-party bots cannot weaponize unpatched issues.

## 2. Coordinated Vulnerability Disclosure (CVD)
- When our static/dynamic analysis identifies a potential security vulnerability (e.g., SSRF, path traversal, auth bypass, or GitHub Actions `pull_request_target` injection via `zizmor`), we **never** open a public Issue or uncoordinated public Pull Request.
- We report exclusively via the upstream project's private **GitHub Security Advisories (GHSA)** or designated `SECURITY.md` contact email.

## 3. Contact
- **Security & Principal Engineering Lead**: **Justin Aharoni** (`contact@jaharoni.com`)
