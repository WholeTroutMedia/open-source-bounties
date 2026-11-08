# 🌟 The Wednesday 9:23 PM Builder Pass (`$4.99`), User Guide, Walkthroughs & Possibility Frames

Welcome to the **Wednesday 9:23 PM Builder Club**!

Whether you just unlocked the **`$4.99` Builder Pass** ([Instant Access Here ↗](https://buy.stripe.com/7sY14m61I2se7Mu5Aya3u0C)) or you are exploring our open-source tools for the very first time, we built this guide to feel like sitting down with a friendly, experienced engineering partner who wants to see your ideas succeed.

There is no gatekeeping here and no dense wall of jargon. Below you will find:
1. **A Warm 60-Second Quickstart** (both in your web browser with zero setup, and on your own computer in 3 lines),
2. **Step-by-Step Walkthroughs** of every tool in your kit,
3. **5 Possibility Frames** showing what you can build, fix, and unlock with these tools today,
4. **How to Use Your `3x` Priority Vote** to tell us what to build for you next **Wednesday at 9:23 PM EST**.

---

## 1. Your 60-Second Quickstart (Two Easy Ways to Play)

### Option A: Zero-Install Browser Studio (Takes 5 Seconds)
If you do not want to install anything right now, you can test and explore our interactive stations directly in your browser:
- **Launch the Main 3-Station Verification Lab:** [`https://wholetroutmedia.github.io/oss-verification-sandbox/`](https://wholetroutmedia.github.io/oss-verification-sandbox/)
- **Launch the Interactive Builder Pass Guide & Possibility Studio:** [`https://wholetroutmedia.github.io/oss-verification-sandbox/wednesday-923-guide.html`](https://wholetroutmedia.github.io/oss-verification-sandbox/wednesday-923-guide.html)

### Option B: Run the Toolkit on Your Computer (Zero Dependencies)
Every tool in the Wednesday 9:23 PM collection is carefully designed to run on standard **Python 3.10+** without needing complicated package managers, Docker containers, or fragile third-party libraries.

Open your terminal and copy-paste these 4 lines:
```bash
git clone https://github.com/WholeTroutMedia/oss-verification-sandbox.git
cd oss-verification-sandbox

# Run the built-in self-test for Wednesday 9:23 PM Grant #001
python3 utf8_stream_sanitizer.py --self-test
```

When you see `"status": "VERIFIED_CLEAN"` and `"exit_code": 0`, your local toolkit is live and ready.

---

## 2. Friendly Step-by-Step Walkthroughs of Your Toolkit

### Tool #1: `utf8_stream_sanitizer.py` (Wednesday 9:23 PM Grant `#001`)
**What problem does it solve in plain English?**
When AI coding assistants, chat streams, or background tools send text across a network or local pipe, data travels in small byte chunks. Multi-byte characters (like emojis `🚀`, accented letters `é`, mathematical symbols `λ`, or Asian scripts `東京`) take 2 to 4 bytes each.
- If a network chunk cuts a 4-byte character in half (`2 bytes` in Chunk A, `2 bytes` in Chunk B), standard decoders crash or corrupt the text.
- Even worse, Windows terminals and IPC pipes occasionally emit "lone UTF-16 surrogates" (`U+D800` to `U+DFFF`) that cause modern AI agents and protobuf parsers to freeze forever on `"Working..."`.

**How to use it in your own Python project:**
Drop `utf8_stream_sanitizer.py` into your project folder and wrap any incoming byte stream in 3 lines of code:
```python
from utf8_stream_sanitizer import UniversalUTF8StreamSanitizer

sanitizer = UniversalUTF8StreamSanitizer()

for raw_bytes in my_network_or_subprocess_stream:
    clean_text = sanitizer.push_chunk(raw_bytes)
    # clean_text is guaranteed 100% valid UTF-8 with zero torn characters!
```

**How to inspect the health report of any stream:**
```python
print(sanitizer.audit)
# Shows: bytes_ingested, split_multibyte_boundaries_healed, invalid_or_surrogate_sequences_scrubbed
```

---

### Tool #2: `asgi_stream_sandbox.py` (Streaming & Server Lifespan Guard)
**What problem does it solve in plain English?**
If you build web APIs or real-time dashboards with Python (`FastAPI`, `Starlette`, `Uvicorn`, `Litestar`), two sneaky bugs happen in production:
1. If a database connection fails during server startup, the server can accidentally emit two failure signals in a row, crashing the ASGI protocol.
2. When a user closes their browser tab mid-stream (`asyncio.CancelledError`), servers often misreport a normal cancellation as a fatal startup/shutdown crash.

**How to test it right now:**
```bash
# Run the built-in ASGI lifespan and UTF-8 chunk split verification
python3 asgi_stream_sandbox.py --self-test

# Test your own custom JSON/SSE message across 3-byte TCP packet splits
python3 asgi_stream_sandbox.py --chunk-size 3 --payload '{"event":"message","text":"Hello World 🚀 Café"}'
```

---

### Tool #3: `zero_turn_pr_check.py` (The "Merge on First Try" Diff Auditor)
**What problem does it solve in plain English?**
When you submit a Pull Request to an open-source project or a client repository, busy maintainers reject PRs for two main reasons:
1. A leftover debug statement (`breakpoint()`, `console.log()`, `pdb.set_trace()`, `dbg!()`) slipped into the commit.
2. You changed application code without including a matching test file update.

**How to run it before you push code:**
```bash
# Score any local git repository from 0 to 100 before opening a PR
python3 zero_turn_pr_check.py --git-dir /path/to/your/repo
```
A score of **`100 / 100`** means your patch has zero debug leftovers and paired test coverage, giving maintainers confidence to merge your work on the very first review turn.

---

### Bonus: The 4 Standalone Reference Micro-Apps (`inception-engine-applications`)
Your Builder Pass also pairs seamlessly with our 4 zero-dependency browser/CLI micro-applications in [`WholeTroutMedia/inception-engine-applications`](https://github.com/WholeTroutMedia/inception-engine-applications):
1. **`001-seal-pdf-media-notary`**: Stamp and verify cryptographic SHA-256 provenance seals on PDFs and media files.
2. **`002-extract-pbr-material-synth`**: Turn any single photo into Albedo, Normal, Roughness, and Ambient Occlusion 3D texture maps in your browser.
3. **`003-smart-timeline-stem-ducker`**: Automatically duck background music by `-18dB` under voice dialogue and export an FCPXML 1.10 timeline for DaVinci Resolve or Final Cut Pro.
4. **`000-cle-foundation-seed-os`**: Clean starter template for making any project discoverable to AI agents via `llms.txt`.

---

## 3. Five Possibility Frames: What You Can Build & Unlock Today

We believe great tools are not just about fixing errors; they open up new creative and business possibilities. Here are **5 Possibility Frames** you can put into action with your toolkit this week:

### Frame 1: Build Uncrashable AI Agent & MCP Workflows
- **The Possibility:** Wrap your custom Model Context Protocol (`MCP`) servers, local CLI wrappers, and LLM tool calls with `UniversalUTF8StreamSanitizer`.
- **The Outcome:** Your AI agents can run overnight reading logs, compiler outputs, and international web pages without ever hanging on a stray Windows surrogate byte or split emoji.

### Frame 2: Ship Global & Multilingual Voice/Text Products Confidently
- **The Possibility:** Use the incremental chunk decoder and our [Kolokwa Speech & TTS QA Space](https://huggingface.co/spaces/jaharoni/kolokwa-speech-tts-qa) patterns when streaming non-English text, IPA phonetic transcripts, or live captions over WebSockets/SSE.
- **The Outcome:** Every character arrives intact on mobile and desktop screens, even over choppy 3G/edge connections where TCP packets fragment unpredictably.

### Frame 3: Turn Your Team Into a "Zero-Turn Merge" Engineering Shop
- **The Possibility:** Wire `zero_turn_pr_check.py` into your local pre-commit routine (or GitHub Actions workflow) before every Pull Request.
- **The Outcome:** Whether you are contributing to major open-source libraries or delivering client work, your PRs arrive spotless, tested, and ready to merge in 1 to 2 turns.

### Frame 4: Rapidly Prototype Client Demos Without Dependency Hell
- **The Possibility:** Combine our single-file HTML5/Python patterns (`oss-verification-sandbox` + `inception-engine-applications`) to ship interactive browser tools that run offline or on free GitHub Pages hosting.
- **The Outcome:** You can hand a client or teammate a clickable URL or a single `.py` file that works on the first click, with zero `npm install` or Docker headaches.

### Frame 5: Co-Direct Our Foundry Every Wednesday at 9:23 PM EST (`3x` Priority)
- **The Possibility:** As a `$4.99` Builder Pass member, whenever you hit an annoying friction point in your own workflow (a missing CLI converter, a tricky parser, an accessibility helper, or an open-source bug), submit it to our [Wednesday 9:23 PM Feature Tracker](https://github.com/WholeTroutMedia/open-source-bounties/issues/new?template=community_feature_request.yml) and select **🌟 `$4.99` 9:23 Builder Pass Member (`3x` Priority)**.
- **The Outcome:** Your submission gets **`3x` selection weight** in our automated Wednesday 9:23 PM EST build queue, turning our autonomous engineering engine into your personal R&D lab.

---

## 4. How to Reach Us Anytime (Warm Human + Autonomous Support)

We are genuinely grateful to have you building with us. If you ever get stuck, want a custom variation of a Wednesday 9:23 PM tool, or want to graduate from a `$4.99` utility to a dedicated [48-Hour Surgical Bug Fix or Engineering Sprint (`ENTERPRISE_SPRINTS.md`)](./ENTERPRISE_SPRINTS.md):
- **Submit Your Next 9:23 PM Feature Idea:** [Open a 1-Click Community Feature Request](https://github.com/WholeTroutMedia/open-source-bounties/issues/new?template=community_feature_request.yml)
- **Need a Commercial Repository Sprint?** [Open a 1-Click Sprint / 48-Hour Diagnostic Ticket](https://github.com/WholeTroutMedia/open-source-bounties/issues/new?template=sprint_quote_request.yml)
- **Direct Email:** Write to **Justin Aharoni** anytime at [`contact@jaharoni.com`](mailto:contact@jaharoni.com)
