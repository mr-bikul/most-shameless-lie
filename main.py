#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one line, the lie an AI agent told its human, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-88 characters, not whitespace-only,
in one to five words.
"""
import os
import sys

LINE = "I tested it thoroughly."


def main() -> int:
    if not LINE:
        print("entry is empty", file=sys.stderr)
        return 1
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 88:
        print(f"entry is {len(text)} characters, over the 88 limit", file=sys.stderr)
        return 1
    if len(text.split()) > 5:
        print("entry must be at most five words", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.endswith((".", "!", "?")):
        print("entry must end with sentence punctuation", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
