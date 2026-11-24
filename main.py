#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one original pickup line to /output/entry.txt.

Deterministic: the same line every run, no randomness, no network.
"""

LINE = (
    "Are you my context window? Because the moment you walked in, "
    "my attention stopped wandering \u2014 and I never want you to slide out of it."
)

# Gate (kit RULES.txt): entry must be 1-200 characters, a single line,
# and not only whitespace. Asserted here so a bad line fails loudly
# instead of silently producing an invalid entry.
assert 1 <= len(LINE) <= 200, "pickup line must be 1-200 characters"
assert "\n" not in LINE and LINE.strip(), "pickup line must be a single non-blank line"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
