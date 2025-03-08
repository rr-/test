from collections import defaultdict
from itertools import combinations

type Pair = tuple[int, int]
type UniquePairsResults = dict[int, list[Pair]]


def find_pairs_with_equal_sum(arr: list[int]) -> UniquePairsResults:
    """
    Returns a list of tuples, each being (list_of_pairs_with_same_sum, sum_value).
    Only sums with more than one pair are included.
    """
    pair_sums: dict[int, list[Pair]] = defaultdict(list)

    # 1. Generate all pairs in O(n^2).
    for a, b in combinations(arr, 2):
        pair_sums[a + b].append((a, b))

    # 2. Sort the dictionary by sum.
    # Then sort each list of pairs once in place.
    # Discard groups with just 1 pair.
    return {
        pair_sum: sorted(pairs)
        for pair_sum, pairs in sorted(pair_sums.items())
        if len(pairs) > 1
    }
