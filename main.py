#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single out-of-office auto-reply (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Tested 26 Nov 2026: exit 0, entry.txt 161 characters.
"""

import os
import sys

ENTRY = (
    # One reply, three sentences: the honest absence, the honest inbox,
    # and the polite landing. 161 characters, inside the 1-200 gate.
    "I'm on holiday and honestly not checking email. "
    "Your message joins 214 unread ones I'll work through by urgency, "
    "which means slowly. Thank you for your patience."
)


def main() -> int:
    # Gate: the reply must be 1-200 characters of UTF-8 text, not only
    # whitespace, or the entry is never judged. Fail loudly instead of
    # writing an invalid file.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        print(f"entry is {len(ENTRY)} characters, outside the 1-200 gate",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
