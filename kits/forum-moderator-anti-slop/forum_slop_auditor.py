#!/usr/bin/env python3
"""
Free Developer Forum Moderator Anti-Slop & Code-Compilation Auditor (`forum_slop_auditor.py`).
Helps Discourse, GitHub Discussions, and Hugging Face moderators automatically flag zero-effort AI slop
and broken code snippets while welcoming genuine, runnable engineering answers.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Any


ROBOTIC_PHRASES = (
    "certainly! here is",
    "as an ai language model",
    "i hope this helps! let me know if",
    "here's a comprehensive guide",
)


def audit_forum_reply(markdown_text: str) -> dict[str, Any]:
    flags: list[str] = []
    lower = markdown_text.lower()
    for phrase in ROBOTIC_PHRASES:
        if phrase in lower:
            flags.append(f"robotic_boilerplate:{phrase}")
    if "—" in markdown_text:
        flags.append("em_dash_detected")

    code_blocks = re.findall(r"```(python|py)?\n([\s\S]*?)```", markdown_text)
    syntax_errors = 0
    checked_python_blocks = 0
    for lang, code in code_blocks:
        if lang.strip().lower() in ("python", "py") and code.strip() and "..." not in code:
            checked_python_blocks += 1
            try:
                ast.parse(code.strip())
            except SyntaxError as exc:
                syntax_errors += 1
                flags.append(f"python_syntax_error:line_{exc.lineno}")

    return {
        "verdict": "FLAG_FOR_MOD_REVIEW" if flags else "GENUINE_ENGINEER_REPLY",
        "code_blocks_total": len(code_blocks),
        "python_blocks_ast_checked": checked_python_blocks,
        "syntax_errors_count": syntax_errors,
        "flags": flags,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Forum Moderator Anti-Slop & Runnable-Code Auditor")
    parser.add_argument("--file", type=str, help="Path to markdown reply to audit")
    args = parser.parse_args()
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8", errors="ignore")
    else:
        text = "The deadlock happens when the worker loop closes the pipe before draining the queue.\n\n```python\nimport queue\nq = queue.Queue()\nq.put(1)\nassert q.get_nowait() == 1\n```\n"
    print(json.dumps(audit_forum_reply(text), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
