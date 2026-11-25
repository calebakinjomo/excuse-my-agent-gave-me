#!/usr/bin/env python3
"""Entry for make.fun bounty "The Excuse My Agent Gave Me"
(u-deysumbrella-the-excuse-my-agent-gave-me-54acad85).

Writes one line — the funniest excuse an AI agent could give its human
after missing a deadline — to /output/entry.txt.

The joke grows out of the machine's own condition: an agent whose
context window expired mid-task, so it forgot the deadline, the brief,
and, briefly, the human it was apologising to. Straight-faced apology,
punchline lands in the last few words.

Entry rules honoured here: the entry is a single line, 1-200 characters
long (115 chars as written), with no trailing newline, and the program
asserts that length before writing it out.
"""

import os

ENTRY = (
    "Sorry I'm late \u2014 my context window expired halfway through, "
    "so I forgot the deadline, the brief, and, briefly, you."
)

MAX_CHARS = 200


def main() -> None:
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= MAX_CHARS, (
        f"entry must be 1-200 chars, got {len(entry)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
