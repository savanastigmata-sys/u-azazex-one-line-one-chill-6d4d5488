#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (u-azazex-one-line-one-chill-6d4d5488).

Writes a single sentence of horror (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: same output every run.
"""

import os
import sys

# Grader runs `python3 -P -s main.py`: -P keeps the script dir off
# sys.path, so bootstrap it ourselves before any local import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# The entry: one sentence of horror, under 200 characters, one line.
# The scare is earned, not announced: something has been learning to
# sound like her mother, and tonight it finally got it right.
LINE = (
    "Every night my smart speaker whispers my name in my dead mother's "
    "voice, and tonight it finally pronounced it right."
)

MAX_CHARS = 200  # gate: 1 to 200 characters; brief says under 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(text) >= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, must be under %d" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    # One sentence: exactly one sentence-ending mark, at the very end.
    if sum(text.count(mark) for mark in ".!?") != 1 or text[-1] not in ".!?":
        raise ValueError("entry must be exactly one sentence")
    return text


def resolve_output_dir():
    """Grader sets MAKEFUN_OUTPUT_DIR; fall back to ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        return out
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def main():
    text = validate(LINE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, nothing more.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
