#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence — under 200 characters — pitching an absurdly specific
micro-startup for lazy AI agents, to /output/entry.txt.

Deterministic: the sentence is a fixed literal, so every run produces
byte-identical output. Standard library only, no network, no input.
"""

import os

PITCH = (
    "A laundromat for lazy agents' bloated context windows, folding a "
    "100k-token conversation into a tidy 500-token summary for $0.25 a wash."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
