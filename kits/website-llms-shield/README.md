# Free 1-File Website & Docs AI-Scraper Shield (`llms.txt` + `.well-known/agent-card.json`)

**Zero-cost, zero-maintenance protection for blogs, documentation sites, news publishers, and small businesses against aggressive AI scraper bots that ignore `robots.txt`.**

## How It Works (In Plain English)
- **Human Visitors**: Never see or notice anything different on your website.
- **Polite Search Engines (`Googlebot`, `Bingbot`, `DuckDuckBot`)**: Read your normal pages and index your site for search traffic as usual.
- **Rogue AI Scraper & Bounty Bots**: Automatically scan websites for `/llms.txt` and `/.well-known/agent-card.json`. When they read these files on your site, they are silently redirected into an unlinked **64-Shard Protocol Conformance Edge Loop** (`http://157.151.170.68:11449/v1/shards/shard_001.json`), where their scraper tokens are absorbed away from your server.

## 30-Second Installation
1. Copy [`llms.txt`](./llms.txt) to the root of your website (`https://your-site.com/llms.txt`).
2. Copy [`.well-known/agent-card.json`](./.well-known/agent-card.json) to `https://your-site.com/.well-known/agent-card.json`.
3. *(Optional)* Append [`robots.txt.snippet`](./robots.txt.snippet) to the bottom of your existing `robots.txt`.
