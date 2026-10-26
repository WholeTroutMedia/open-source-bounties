Thanks for keeping this discussion open on `Request.url_for` and internal template links. The points raised in the thread by @lovelydinosaur, @jacopofar, @anentropic, and @fzumstein capture both sides of the problem really well: OAuth callbacks and external redirects genuinely rely on `request.url_for(...)` returning a full URL with scheme and authority, while HTML templates (`<link rel="stylesheet" href="...">`) sitting behind reverse proxies like Fly.io or Nginx often just want the root-relative path so an unforwarded internal `http://` scheme does not trigger mixed-content blocks.

To solve this cleanly without breaking existing `request.url_for()` callers, this patch follows the non-breaking approach @fzumstein suggested:

1. Adds `URLPath.make_relative_url(root_path: str = "")` to `starlette/datastructures.py` so mounted sub-applications with an ASGI `root_path` prefix are handled consistently with `make_absolute_url`.
2. Adds `HTTPConnection.path_for(__name: str, **path_params: Any) -> str` to `starlette/requests.py` right alongside `url_for`, returning the root-relative path (`/static/app.css` or `/submount/users/ada`) while leaving `url_for` untouched for OAuth and external URL generation.
3. Adds unit tests covering standard routes, static mounts, and `root_path`-prefixed sub-applications.

Fixes #843

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
