"""Everyday Wonder entry: one sentence on a small moment of wonder.

Writes a single sentence (1-200 characters) to entry.txt in the output
directory: $ENTRY_OUTPUT_DIR, or /output when unset. Stdlib only, no
network, fully deterministic.
"""

import os

LINE = (
    "The lift mirror yawned half a second before I did, "
    "and I apologised to the stranger before realising it was me."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
