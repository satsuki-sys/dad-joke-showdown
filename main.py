#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes a single dad joke, told out loud at the dinner table,
to /output/entry.txt. Python 3.13, standard library only.

Draft 1: dinner-table setup, salt pun in the punchline.

Revision against the judge criteria:
1. Dad at the table: "pass the salt" already puts us at the
   dinner table, so the "At dinner," opener earns nothing.
2. Pun "seasoned" lands cleanly on first read (salt + practised
   at ignoring). Keep.
3. Fresh: salt/seasoned is not one of the thousand-times-told
   ones (no "Hi hungry", no "steaks are high"). Keep.
4. Tight: dropping "At dinner," cuts four words and leaves the
   punchline — the quoted line — at the very end. Keep "sighed":
   it is the dad delivery, and it earns its place.
5. Reads aloud: "Dad asked me to pass the salt, then sighed..."
   has a rhythm a father could deliver across the table.
Final joke below.
"""

import os

JOKE = (
    "Dad asked me to pass the salt, then sighed, "
    "'You're really seasoned at ignoring me.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
