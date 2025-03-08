import sys
from contextlib import contextmanager
from io import StringIO
from tempfile import NamedTemporaryFile
from typing import Iterator
from unittest.mock import Mock, call, patch

from .__main__ import format_unique_pairs_output, main, process_numbers


@contextmanager
def stub_stdin(input: str) -> Iterator[None]:
    real_stdin = sys.stdin
    sys.stdin = StringIO(input)
    yield
    sys.stdin = real_stdin


def test_format_unique_pairs_output_no_pairs() -> None:
    assert format_unique_pairs_output({}) == "No pairs"


def test_format_unique_pairs_output_with_pairs() -> None:
    rseults = {3: [(1, 2), (3, 4)], 11: [(5, 6)]}
    expected_output = (
        "Pairs : ( 1, 2) ( 3, 4) have sum : 3\n"
        "Pairs : ( 5, 6) have sum : 11"
    )
    assert format_unique_pairs_output(rseults) == expected_output


@patch("builtins.print")
def test_main_with_data(mock_print: Mock) -> None:
    with stub_stdin("1 2 3 4 5\n5 10 15 20\n"), patch("sys.argv", [""]):
        main()
    mock_print.assert_has_calls(
        [
            call("Enter numbers to analyze.", file=sys.stderr),
            call(
                "Pairs : ( 1, 4) ( 2, 3) have sum : 5\n"
                "Pairs : ( 1, 5) ( 2, 4) have sum : 6\n"
                "Pairs : ( 2, 5) ( 3, 4) have sum : 7"
            ),
            call("Pairs : ( 5, 20) ( 10, 15) have sum : 25"),
        ]
    )


@patch("builtins.print")
def test_main_with_tempfile(mock_print: Mock) -> None:
    with NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write("1 2 3 4 5\n5 10 15 20\n")
        temp_file.seek(0)

        with patch("sys.argv", ["", "-f", temp_file.name]):
            main()

    mock_print.assert_has_calls(
        [
            call(
                "Pairs : ( 1, 4) ( 2, 3) have sum : 5\n"
                "Pairs : ( 1, 5) ( 2, 4) have sum : 6\n"
                "Pairs : ( 2, 5) ( 3, 4) have sum : 7"
            ),
            call("Pairs : ( 5, 20) ( 10, 15) have sum : 25"),
        ]
    )


@patch("builtins.print")
def test_process_numbers_with_invalid_input(mock_print: Mock) -> None:
    with stub_stdin("1 2 three 4\n5 6 7 8\n"):
        process_numbers(sys.stdin)
    mock_print.assert_has_calls(
        [
            call(
                "Invalid input (invalid literal for int() with base 10: 'three')",
                file=sys.stderr,
            ),
            call("Pairs : ( 5, 8) ( 6, 7) have sum : 13"),
        ]
    )
