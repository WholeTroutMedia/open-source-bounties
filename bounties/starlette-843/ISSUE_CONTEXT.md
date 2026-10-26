# Upstream Bounty Context: `Kludex/starlette#843`

- **Upstream Issue**: [https://github.com/Kludex/starlette/issues/843](https://github.com/Kludex/starlette/issues/843)
- **Repository**: `Kludex/starlette` (`12,685` stars, Python ASGI framework)
- **Funding Platform**: Polar.sh Community Pledge Pool
- **Difficulty Tier**: `Easy`
- **Target Branch**: `master`

## Problem Statement
`Request.url_for(name, **path_params)` always constructs a full URL with scheme and authority (`http://...`) via `URLPath.make_absolute_url(base_url=self.base_url)`. When rendering HTML templates behind reverse proxies (such as Fly.io, Nginx, or Cloudflare tunnels) or linking to internal routes, callers frequently want the root-relative path (`/static/style.css` or `/users/42`) without coupling links to the internal `Host` header, while keeping full backward compatibility for existing `Request.url_for` callers (such as OAuth redirect callbacks).
