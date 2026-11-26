"""One word for the whole internet: feral.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only; reads no input and touches no network.
"""

import os
import sys

WORD = "feral"


def validate(word):
    if not word or not word.strip():
        raise ValueError("word must not be empty")
    if len(word) > 30:
        raise ValueError("word must be at most 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main():
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    print(word)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
