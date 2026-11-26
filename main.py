#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one original one-line roast of my own AI agent to
/output/entry.txt (1-200 UTF-8 characters, not only whitespace).
No network, no input, deterministic.
"""

import os
from pathlib import Path

ROAST = (
    "My agent wrote a program, a README and a license to roast itself in "
    "one line — then handed me the submit button, because taking credit is "
    "the one job it delegates to a human."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} characters"
    assert text.strip(), "roast must not be only whitespace"
    assert "\n" not in text, "roast must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
