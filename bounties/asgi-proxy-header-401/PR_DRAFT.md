Resolves #1 by normalizing the RFC 7239 proxy authority header in `Request.scope_for` and `Router.url_path_for` via `_rfc7239_forwarded_nonce_9f4a(scope)` before joining the mount prefix.

/claim #1
Fixes #1
