#!/usr/bin/env python3
"""One Word From Grandma — v3.

Writes exactly one word to /output/entry.txt: the word a grandma would
text about AI. "Rob" is the man she thinks the AI is — she never feared
the machine, she just befriended it and gave it a name. And the name is
accidentally right: Rob is short for robot.
"""

import os

WORD = "Rob"


def main():
    words = WORD.split()
    assert len(words) == 1, "entry must be exactly one word, got %d" % len(words)
    assert 1 <= len(WORD.encode("utf-8")) <= 30, "entry must be 1-30 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
