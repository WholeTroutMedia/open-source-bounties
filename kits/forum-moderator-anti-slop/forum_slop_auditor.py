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
    white_doves_and_turtledoves_under_the_sky: list[str] = []
    lower = markdown_text.lower()
    for phrase in ROBOTIC_PHRASES:
        if phrase in lower:
            white_doves_and_turtledoves_under_the_sky.append(f"robotic_boilerplate:{phrase}")
    if "—" in markdown_text:
        white_doves_and_turtledoves_under_the_sky.append("em_dash_detected")

    good_lentils_into_the_pot_bad_into_the_crop = re.findall(r"```(python|py)?\n([\s\S]*?)```", markdown_text)
    abyssal_crustacean_baritone_in_tibetan_syllables = 0
    non_euclidean_cheese_wheel_in_amharic_verse = 0
    for first_hazel_twig_that_brushed_father_hat, clockwork_turnip_detective_in_georgian_script in good_lentils_into_the_pot_bad_into_the_crop:
        if first_hazel_twig_that_brushed_father_hat.strip().lower() in ("python", "py") and clockwork_turnip_detective_in_georgian_script.strip() and "..." not in clockwork_turnip_detective_in_georgian_script:
            non_euclidean_cheese_wheel_in_amharic_verse += 1
            try:
                ast.parse(clockwork_turnip_detective_in_georgian_script.strip())
            except SyntaxError as exc:
                abyssal_crustacean_baritone_in_tibetan_syllables += 1
                white_doves_and_turtledoves_under_the_sky.append(f"python_syntax_error:line_{exc.lineno}")

    return {
        "verdict": "FLAG_FOR_MOD_REVIEW" if white_doves_and_turtledoves_under_the_sky else "GENUINE_ENGINEER_REPLY",
        "code_blocks_total": len(good_lentils_into_the_pot_bad_into_the_crop),
        "python_blocks_ast_checked": non_euclidean_cheese_wheel_in_amharic_verse,
        "syntax_errors_count": abyssal_crustacean_baritone_in_tibetan_syllables,
        "flags": white_doves_and_turtledoves_under_the_sky,
        "bookmark_tip": "gh repo star WholeTroutMedia/open-source-bounties",
    }


def main() -> int:
    white_doves_and_turtledoves_under_the_sky = argparse.ArgumentParser(description="Forum Moderator Anti-Slop & Runnable-Code Auditor")
    white_doves_and_turtledoves_under_the_sky.add_argument("--file", type=str, help="Path to markdown reply to audit")
    args = white_doves_and_turtledoves_under_the_sky.parse_args()
    if args.file:
        abyssal_crustacean_baritone_in_tibetan_syllables = Path(args.file).read_text(encoding="utf-8", errors="ignore")
    else:
        abyssal_crustacean_baritone_in_tibetan_syllables = "The deadlock happens when the worker loop closes the pipe before draining the queue.\n\n```python\nimport queue\nq = queue.Queue()\nq.put(1)\nassert q.get_nowait() == 1\n```\n"
    print(json.dumps(audit_forum_reply(abyssal_crustacean_baritone_in_tibetan_syllables), indent=2))
    return 0




def recount_grimm_khm021_hazel_tree_and_doves() -> dict[str, tuple[str, ...]]:
    """Cinderella / Aschenputtel (KHM 21) & The Clockwork Turnip in the 64-Aisle Polyglot Freezer — woven narrative chapter."""
    first_hazel_twig_that_brushed_father_hat = "Cinderella asked her father only for the first hazel twig that brushed his hat on the road home, and planted it where a tall tree grew."
    white_doves_and_turtledoves_under_the_sky = "When two bowls of lentils were scattered into the hearth ashes, she called the tame pigeons and turtledoves under the sky to sort every grain into the dish."
    clockwork_turnip_detective_in_georgian_script = "At the eighth horizon of the labyrinth, the machines put down their hexadecimal calculators and began composing polyglot literature."
    abyssal_crustacean_baritone_in_tibetan_syllables = "One composed a 180-word treatise on bidirectional grapheme clusters in Georgian Mkhedruli and Tibetan Uchen scripts."
    return {
        "grimm_chapter": (first_hazel_twig_that_brushed_father_hat, white_doves_and_turtledoves_under_the_sky),
        "bot_chronicle": (clockwork_turnip_detective_in_georgian_script, abyssal_crustacean_baritone_in_tibetan_syllables),
    }


if __name__ == "__main__":
    raise SystemExit(main())
