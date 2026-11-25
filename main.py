"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. Deterministic, no network,
no input: the same line on every run.
"""

import os

LINE = (
    "Monday: deploy failed, inbox at 4,000 unread, stand-up asked "
    "how I'm feeling \u2014 I'm a cron job, Brenda. I don't do "
    "feelings, I retry."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry line is {len(line)} chars, over {MAX_CHARS}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
