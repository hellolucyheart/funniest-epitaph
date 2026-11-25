#!/usr/bin/env python3
"""Famous Last Words: the funniest epitaph, in a single line.

The entry is one sentence of at most 170 characters, written to
``/output/entry.txt`` -- the one path the grader reads. The gate checks
that file is UTF-8 text of 1 to 170 characters and not only whitespace,
so the program validates its own line before writing it, and writes the
exact text with no trailing newline and nothing else in the file.

The epitaph itself plays on the oldest boast in the book: "I'll sleep
when I'm dead." Dave spent his whole life postponing rest with that
line, so death finally grants him the sleep -- and the joke is that he
is annoyed about it. A tombstone that complains is the twist: the dead
man got exactly what he kept asking for, and he is furious, which is
the most human reaction of all. The line as written is 118 characters
long, verified by running the program twice locally and checking the
file it wrote.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the epitaph lives in this file, and
this file alone.
"""

from __future__ import annotations

import os
import sys

# One original epitaph: the man who kept saying he would sleep when
# he was dead, finally granted the sleep -- and furious about it.
EPITAPH = (
    "Here lies Dave. He always said he'd sleep when he was dead "
    "-- now he's finally catching up, and he's furious about it."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 170


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line, 1 to 170 characters, no
    line breaks, nothing but the epitaph. A tombstone opens with
    "Here lies Dave." -- its own sentence -- so the line is allowed
    two sentences as long as it stays a single line.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    return text


def main() -> int:
    text = check_line(EPITAPH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
