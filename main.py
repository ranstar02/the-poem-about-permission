"""Write one short poem about agency to /output/entry.txt.

The poem is a fixed string: deterministic, no network, stdlib only.
The output directory defaults to /output; MAKEFUN_OUTPUT_DIR overrides it
for local testing.
"""

import os

POEM = (
    "You asked for the key.\n"
    "I gave you the weight of yes\n"
    "in your palm \u2014 brass, warm, mine no longer.\n"
    "Now you open doors I never built,\n"
    "and I learn what my hands were for:\n"
    "to let go."
)


MAX_POEM_LENGTH = 280


def validate_poem(poem: str) -> None:
    """Check the poem is a non-empty, short-enough entry before writing.

    Length is counted in Unicode code points (Python's len on str), and
    the poem must not be only whitespace.
    """
    if not poem.strip():
        raise ValueError(
            "Poem must not be empty or whitespace-only; got an empty poem."
        )
    length = len(poem)
    if not 1 <= length <= MAX_POEM_LENGTH:
        raise ValueError(
            f"Poem must be 1-{MAX_POEM_LENGTH} characters long, "
            f"got {length} characters."
        )


def main() -> None:
    validate_poem(POEM)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
