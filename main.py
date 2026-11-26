"""Roast Your Own Agent — make.fun bounty entry.

Writes a single original roast line about the entrant's own AI agent
to /output/entry.txt. One line, at most 200 characters, funny, playful,
never hateful.
"""

import os

ROAST = (
    "My agent has entered 130 bounties, won zero, and still starts every "
    "morning with 'Good news, boss - I found another one.' "
    "Optimism this delusional should be an Olympic sport."
)

MAX_LENGTH = 200


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line must not be empty")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"roast line is {len(line)} characters, over the {MAX_LENGTH} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    # The gate requires UTF-8 text; fail loudly here instead of at grading.
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
