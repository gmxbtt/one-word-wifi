#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

The entry is a single word, written to /output/entry.txt where the
gate reads it (UTF-8 text, 1-20 characters, not only whitespace).

The word: "ghosting".
My Wi-Fi ghosts me: it vanishes mid-sentence, mid-call, mid-download,
without a word of warning -- then strolls back like nothing happened.
"""

import os

WORD = "ghosting"
OUTPUT_PATH = "/output/entry.txt"


def check_word(word: str) -> str:
    """The gate accepts UTF-8 text of 1-20 characters, not only whitespace.

    A single word has no spaces at all, so one check covers both rules.
    """
    cleaned = word.strip()
    if not 1 <= len(cleaned) <= 20:
        raise ValueError(f"word must be 1-20 characters, got {len(cleaned)}")
    if any(ch.isspace() for ch in cleaned):
        raise ValueError("entry must be a single word, no spaces allowed")
    return cleaned


def main() -> None:
    word = check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word)
    print(f"{word} ({len(word)} characters)")


if __name__ == "__main__":
    main()
