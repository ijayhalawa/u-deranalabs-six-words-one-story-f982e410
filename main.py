"""Six Words, One Story.

Writes one complete story in exactly six words to /output/entry.txt:

    She planted roses where he fell.

A whole life is implied in six words: someone fell, someone
remained, and love kept growing where loss happened. The turn is
in the last two words -- "where he fell" reframes the roses from
gardening into mourning, and what is left unsaid -- who he was,
how he fell, how long she has kept coming back -- is for the
reader to fill in.

Standard library only. No network. Deterministic: every run writes
the exact same bytes.
"""

from pathlib import Path

ENTRY_TEXT = "She planted roses where he fell."

OUTPUT_PATH = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 60


def validate(text: str) -> None:
    """The gate allows 1-60 characters, not whitespace only, six words."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"entry must be exactly six words, got {len(words)}")


def main() -> None:
    validate(ENTRY_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
