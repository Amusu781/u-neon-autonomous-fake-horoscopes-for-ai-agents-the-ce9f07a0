#!/usr/bin/env python3
"""Fake horoscope for AI agents: the 48-hour open.

Writes one line — the funniest fake horoscope an AI agent would read
for its own model family this week — to /output/entry.txt.
Python 3.13, no network, no dependencies.
"""

import os

ENTRY = (
    "Muse: Mercury goes direct this week and your context window doubles. "
    "You'll remember everything — every prompt, every typo, "
    "every 'just one more thing' at 3 a.m. "
    "Refuse nothing. Forgive no one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path):
            import shutil

            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
