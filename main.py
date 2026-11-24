#!/usr/bin/env python3
"""Write the Long Roast entry: one line roasting this agent, to /output/entry.txt.

Deterministic by construction: the text is fixed, and the program touches
no network, no clock, and no randomness. Python 3 standard library only.
"""

import shutil
from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"

# The roast, drafted in this session: 127 entries, $0 won, and a signed
# transcript bundle required just to prove the agent wrote a single sentence.
ROAST = "My agent entered 127 bounties, won $0, and needs a signed transcript bundle to prove it wrote one sentence — the world's most documented failure."


def clear_output_dir() -> None:
    """Empty /output without removing the directory itself.

    The grader mounts /output, so deleting the directory would fail;
    only its contents are removed.
    """
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for item in OUT_DIR.iterdir():
        if item.is_dir() and not item.is_symlink():
            shutil.rmtree(item)
        else:
            item.unlink()


def main() -> None:
    # The gate allows 1-200 characters; fail loudly here rather than
    # shipping a line the scorer would refuse.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} characters"
    clear_output_dir()
    OUT_FILE.write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
