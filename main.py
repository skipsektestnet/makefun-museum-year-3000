#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label for an everyday object."""

import os

ENTRY_TEXT = "Plastic Fork, c. 2025. Built to outlive its owner by four centuries, used for nine minutes, then buried with full honours in a landfill the size of Belgium."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write(ENTRY_TEXT)
    print(f"entry.txt: {len(ENTRY_TEXT)} characters")


if __name__ == "__main__":
    main()
