#!/usr/bin/env python3
"""Write one sick-day excuse to entry.txt.

The excuse is a single line, chosen to be half believable, fresh, and to
land its laugh just before the last word. This program is deterministic:
it always writes the same line, validates it against the competition gate
(1-200 characters, single line, non-blank, valid UTF-8), and writes it
with no trailing newline to MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

# The excuse: a sneeze strong enough to pull a muscle is the kind of
# injury a boss half believes and a coworker quotes all week. Kept in
# plain ASCII so the byte count and the character count agree exactly.
ENTRY = "Won't be in today, I sneezed so hard I pulled something and now I'm the guy who got injured by his own face."


def validate(text):
    """Check the line against the sealed gate; exit non-zero if it fails."""
    if not text or not text.strip():
        sys.exit("error: entry is blank")
    if len(text) > 200:
        sys.exit(f"error: entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        sys.exit("error: entry must be a single line")
    if text != text.strip():
        sys.exit("error: entry has leading or trailing whitespace")
    text.encode("utf-8")  # raises if not encodable


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
