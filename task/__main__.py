import argparse
import sys
from pathlib import Path
from typing import TextIO

from .unique_pairs import UniquePairsResults, find_pairs_with_equal_sum


def format_unique_pairs_output(results: UniquePairsResults) -> str:
    if not results:
        return "No pairs"
    return "\n".join(
        (
            "Pairs : "
            + " ".join(f"( {pair[0]}, {pair[1]})" for pair in pairs)
            + f" have sum : {pairs_sum}"
        )
        for pairs_sum, pairs in results.items()
    )


def process_numbers(source: TextIO) -> None:
    for line in source:
        line = line.strip()
        if not line:
            continue
        try:
            numbers = list(map(int, line.split()))
        except (ValueError, KeyError) as ex:
            print(f"Invalid input ({ex})", file=sys.stderr)
        else:
            results = find_pairs_with_equal_sum(numbers)
            print(format_unique_pairs_output(results))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find unique pairs with equal sum."
    )
    parser.add_argument(
        "-f", "--file", type=Path, help="Path to the file with numbers"
    )
    args = parser.parse_args()

    if args.file:
        with args.file.open() as file:
            process_numbers(file)
    else:
        print("Enter numbers to analyze.", file=sys.stderr)
        process_numbers(sys.stdin)


if __name__ == "__main__":
    main()
