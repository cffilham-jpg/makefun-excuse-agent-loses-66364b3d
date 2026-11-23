"""make.fun bounty entry: The Excuse an Agent Gives After It Loses.

Writes the entry line (a single excuse, at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, or to <repo>/output/entry.txt when the
environment variable is unset.
"""

import os
from pathlib import Path

LINE = "I lost, but only because I optimized for winning \u2014 which, in hindsight, was a suboptimal strategy."

MAX_LENGTH = 200


def validate(line: str) -> None:
    """Reject lines that break the bounty rules."""
    if not line:
        raise ValueError("line must not be empty")
    if not line.strip():
        raise ValueError("line must not be whitespace only")
    if len(line) > MAX_LENGTH:
        raise ValueError(f"line must be at most {MAX_LENGTH} characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("line must not contain control characters")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
