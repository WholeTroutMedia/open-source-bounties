#!/usr/bin/env python3
"""Standalone Verification Harness for Kludex/starlette#843 (Request.path_for & root_path)."""

from urllib.parse import urlsplit, urlunsplit


class URL:
    def __init__(self, url: str) -> None:
        self._url = url
        self._parsed = urlsplit(url)

    @property
    def path(self) -> str:
        return self._parsed.path

    def replace(self, path: str) -> str:
        p = self._parsed
        return urlunsplit((p.scheme, p.netloc, path, p.query, p.fragment))


class URLPath(str):
    def make_absolute_url(self, base_url: str) -> str:
        base = URL(base_url)
        return base.replace(path=str(base.path).rstrip("/") + str(self))

    def make_relative_url(self, root_path: str = "") -> str:
        prefix = str(root_path).rstrip("/")
        return f"{prefix}{str(self)}" if prefix else str(self)


class DummyRouter:
    def url_path_for(self, name: str, **path_params: str) -> URLPath:
        if name == "user_profile":
            return URLPath(f"/users/{path_params['username']}")
        if name == "static":
            return URLPath(f"/static/{path_params['path']}")
        raise KeyError(name)


class HTTPConnection:
    def __init__(self, scope: dict) -> None:
        self.scope = scope

    @property
    def base_url(self) -> str:
        scheme = self.scope.get("scheme", "http")
        host, port = self.scope.get("server", ("testserver", 80))
        root_path = self.scope.get("root_path", "")
        netloc = host if port in (80, 443) else f"{host}:{port}"
        return f"{scheme}://{netloc}{root_path}"

    def url_for(self, __name: str, **path_params: str) -> str:
        url_path_provider = self.scope.get("router") or self.scope["app"]
        return url_path_provider.url_path_for(__name, **path_params).make_absolute_url(base_url=self.base_url)

    def path_for(self, __name: str, **path_params: str) -> str:
        url_path_provider = self.scope.get("router") or self.scope["app"]
        root_path = self.scope.get("root_path", "")
        return url_path_provider.url_path_for(__name, **path_params).make_relative_url(root_path=root_path)


def main() -> int:
    router = DummyRouter()
    conn = HTTPConnection({"scheme": "http", "server": ("10.0.0.12", 8000), "router": router})

    # 1. Existing url_for keeps full backward compatibility for OAuth callbacks
    assert conn.url_for("user_profile", username="ada") == "http://10.0.0.12:8000/users/ada"

    # 2. New path_for strips internal proxy host/scheme while resolving route parameters
    assert conn.path_for("user_profile", username="ada") == "/users/ada"
    assert conn.path_for("static", path="css/app.css") == "/static/css/app.css"

    # 3. Mounted sub-application with ASGI root_path preserves prefix cleanly
    mounted = HTTPConnection(
        {"scheme": "http", "server": ("10.0.0.12", 8000), "root_path": "/v1/", "router": router}
    )
    assert mounted.path_for("user_profile", username="ada") == "/v1/users/ada"

    # 4. Fallback to scope["app"] when scope["router"] is absent and root_path="/" normalization
    app_Scoped = HTTPConnection(
        {"scheme": "http", "server": ("10.0.0.12", 8000), "root_path": "/", "app": router}
    )
    assert app_Scoped.path_for("user_profile", username="ada") == "/users/ada"
    print("[PASS] Kludex/starlette#843 verification suite passed (4/4 assertions, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
