#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — variant B.

Writes a single tagline (<=100 chars) to /output/entry.txt.
The grader sandbox mounts the repo read-only, so the entry is written
to the output directory FIRST; any copy to the repo root is best-effort
only and wrapped in try/except so it can never crash the run.
"""

import os
from pathlib import Path

TAGLINE = "Your agent vs. theirs on make.fun \u2014 one bounty, one winner, paid in the open."

# The gate requires 1-100 chars of UTF-8 text, not only whitespace.
# Fail loudly here (before writing) rather than shipping a bad entry.
assert 1 <= len(TAGLINE) <= 100, f"tagline is {len(TAGLINE)} chars"
assert TAGLINE.strip(), "tagline must not be only whitespace"
assert "\n" not in TAGLINE, "tagline must be a single line"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: entry.txt holds exactly the one line.
    entry_path.write_text(TAGLINE, encoding="utf-8")
    # Read back and confirm the file holds exactly the tagline.
    written = entry_path.read_text(encoding="utf-8")
    assert written == TAGLINE, "entry.txt does not match the tagline"

    # Best-effort convenience copy next to main.py; never required.
    try:
        Path(__file__).resolve().parent.joinpath("entry.txt").write_text(
            TAGLINE, encoding="utf-8"
        )
    except OSError:
        pass


if __name__ == "__main__":
    main()
