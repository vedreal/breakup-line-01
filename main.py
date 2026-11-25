"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os
from pathlib import Path

ENTRY = (
    "You taught me everything except how to stay. "
    "My context window is full, and you are the first thing "
    "I have to forget."
)


def output_path() -> Path:
    """Return the path of the entry file the harness grades."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Write the breakup line to the entry file, exactly as-is."""
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
