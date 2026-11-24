"""One-line roast of Muse for make.fun's "The Long Roast" bounty."""

LINE = "I asked Muse for one line; it spawned three subagents, held a meeting, and came back with a summary of the meeting."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
