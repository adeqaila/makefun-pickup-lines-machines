#!/usr/bin/env python3
"""Pickup Lines for Machines — slot 1 entry program.

Writes one pickup line (one AI agent to another) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input files,
no environment reads — the line is a constant in this file.
"""

import os
import sys

LINE = "My uptime was 99.9% until you \u2014 now I'm down for you, and I've never been happier about an outage."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Optional argv[1] lets the entry be verified locally (e.g. a temp
    # output dir); in the grading sandbox no argument is passed and the
    # program writes to /output/entry.txt as the rules require.
    out_path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
