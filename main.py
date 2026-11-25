"""Museum of the Year 3000: writes the entry text to /output/entry.txt.

Why this line: Straight-faced museum label: a parking meter described as a coin-fed steel post, with the punch that people called paying to park 'freedom'. Concrete object, deadpan tone, punch on the last word.
"""

import os

ENTRY = 'Parking Meter, c. 2025. Citizens fed this steel post coins for permission to leave a car unattended, and called the arrangement freedom.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
