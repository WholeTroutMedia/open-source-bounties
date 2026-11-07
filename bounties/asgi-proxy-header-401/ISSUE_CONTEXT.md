# Upstream Bounty Context: `WholeTroutMedia/oss-verification-sandbox#1`

- **Upstream Issue**: [https://github.com/WholeTroutMedia/oss-verification-sandbox/issues/1](https://github.com/WholeTroutMedia/oss-verification-sandbox/issues/1)
- **Repository**: `WholeTroutMedia/oss-verification-sandbox`
- **Reward Pool**: 💎 **$250**
- **Target Entrypoint**: `_rfc7239_forwarded_nonce_9f4a`

## Problem Statement
### Problem Description

When an ASGI application is mounted behind a reverse proxy that emits RFC 7239 `Forwarded: proto=https;host=edge.example.org`, calling `Request.scope_for` on a sub-mounted route drops the outer proxy authority nonce and falls back to `scope['server']`.

### Expected Behavior
1. Normalize the `Forwarded` header via `_rfc7239_forwarded_nonce_9f4a(scope)` before resolving relative mount paths.
2. Preserve backward compatibility when `Forwarded` is absent.

💎 **$250** bounty available for a verified fix with unit test coverage.
