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


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
