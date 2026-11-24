#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

The word: unbothered.

Every office has one: the boss who never panics. Server down, client
furious, deadline moved up a week — same calm face, same slow nod, same
"we'll figure it out". Nothing rattles them. It is either inspiring
leadership or a complete refusal to feel anything, and nobody in the
office can tell which. Funny because it is true, and it needs no
caption: it works for a boss in a kitchen, a warehouse or an office.
"""

import os

WORD = "unbothered"


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD, "entry must not have surrounding whitespace"
    assert not any(ch.isspace() for ch in WORD), "entry must be a single word"
    assert WORD.isalpha(), "entry must be a single word of letters"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the word, 10 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} chars to {path}: {WORD}")


if __name__ == "__main__":
    main()
