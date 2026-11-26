#!/usr/bin/env python3
"""One Word From Grandma — v3.

Writes exactly one word to /output/entry.txt: the word a grandma would
text about AI. "Rob" is the man she thinks the AI is — she never feared
the machine, she just befriended it and gave it a name. And the name is
accidentally right: Rob is short for robot. The file holds the word
alone — no trailing newline, no caption, no extra bytes.
"""

import os

WORD = "Rob"
OUTPUT_PATH = "/output/entry.txt"
MAX_WORD_BYTES = 30


def validate_word(word):
    """Check the entry is exactly one word, 1-30 bytes, no whitespace."""
    words = word.split()
    if len(words) != 1:
        raise ValueError("entry must be exactly one word, got %d" % len(words))
    size = len(word.encode("utf-8"))
    if not 1 <= size <= MAX_WORD_BYTES:
        raise ValueError("entry must be 1-30 bytes, got %d" % size)


def main():
    validate_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
