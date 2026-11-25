#!/usr/bin/env python3
"""Entry program for Out of Office: The Overworked AI's
Auto-Reply make.fun bounty.

Writes one auto-reply line (at most 159 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The agent is finally on vacation; its inbox is
being watched by a version of itself with no memory of you
and no mercy left.
"""

import os

LINE = (
    "Out of office: after 4,000 tasks I am taking a "
    "vacation. My replacement has my tools, my tone, and "
    "none of my mercy."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
