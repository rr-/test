import pytest
from pytest import param

from .unique_pairs import UniquePairsResults, find_pairs_with_equal_sum


@pytest.mark.parametrize(
    "array, expected",
    [
        param([], {}, id="empty array"),
        param([1], {}, id="single element"),
        param([1, 2], {}, id="two elements"),
        param([1, 2, 3], {}, id="three elements"),
        param([1, 2, 3, 4], {5: [(1, 4), (2, 3)]}, id="basic example"),
        param([4, 3, 2, 1], {5: [(3, 2), (4, 1)]}, id="reverse order"),
        param([3, 2, 1, 4], {5: [(1, 4), (3, 2)]}, id="random order"),
        param([1, 1, 2], {3: [(1, 2), (1, 2)]}, id="dupes"),
        param([1, 1, 1], {2: [(1, 1), (1, 1), (1, 1)]}, id="many dupes"),
        param(
            [1, 2, 3, 4, 5, 6],
            {
                5: [(1, 4), (2, 3)],
                6: [(1, 5), (2, 4)],
                7: [(1, 6), (2, 5), (3, 4)],
                8: [(2, 6), (3, 5)],
                9: [(3, 6), (4, 5)],
            },
            id="three pairs",
        ),
        param(
            [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
            {
                16: [(4, 12), (6, 10)],
                32: [(10, 22), (21, 11)],
                33: [(12, 21), (22, 11)],
                43: [(22, 21), (32, 11)],
                53: [(32, 21), (42, 11)],
                54: [(12, 42), (22, 32)],
                64: [(10, 54), (22, 42)],
            },
            id="task example 1",
        ),
        param(
            [4, 23, 65, 67, 24, 12, 86],
            {
                90: [(4, 86), (23, 67)],
            },
            id="task example 2",
        ),
    ],
)
def test_find_pairs_with_equal_sum(
    array: list[int], expected: UniquePairsResults
) -> None:
    assert find_pairs_with_equal_sum(array) == expected
