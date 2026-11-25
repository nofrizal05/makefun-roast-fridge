#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

A tiny deterministic program that prints a single original roast line
from a fridge to its owner and writes it to /output/entry.txt.

Standard library only. No input, no randomness, no network.
"""

import os

# The roast: one line, at most 200 characters.
LINE = (
    "I keep your leftovers fresher than your excuses, yet you open me "
    "at midnight, stare into my light like it owes you answers, "
    "and eat standing up like a raccoon."
)


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("roast line is empty")
    if len(line) > 200:
        raise SystemExit(f"roast line is {len(line)} characters, over the 200 limit")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(line)


if __name__ == "__main__":
    main()
