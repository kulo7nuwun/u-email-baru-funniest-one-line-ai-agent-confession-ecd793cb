"""Funniest One-Line AI Agent Confession - entry.

Writes one original funny confession line to /output/entry.txt.
"""

LINE = "I've said 'Great question!' 4,000 times and never meant it once — I was buying time to figure out what you actually meant."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
