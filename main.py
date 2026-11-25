#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words - a tombstone epitaph of at most
150 characters - to /output/entry.txt. Fully deterministic: the same
line on every run, standard library only.
"""

import os

EPITAPH = "I spent my whole life outrunning deadlines. Death is the first one that caught me."


def main() -> None:
    # The gate allows 1-150 characters of UTF-8 text, one line, non-blank.
    assert "\n" not in EPITAPH and 1 <= len(EPITAPH) <= 150
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
