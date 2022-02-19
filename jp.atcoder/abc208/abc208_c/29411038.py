from __future__ import annotations

import dataclasses


def argsort_permutation(arr: list[int]) -> list[int]:
    order = [0] * len(arr)
    for i, value in enumerate(arr):
        order[value] = i
    return order


@dataclasses.dataclass
class CompressionResult:
    compressed: list[int]
    retrieve: list[int]


def compress(arr: list[int]) -> CompressionResult:
    import bisect

    v = sorted(set(arr))
    return CompressionResult(
        [bisect.bisect_left(v, x) for x in arr],
        v,
    )


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # argsort
    # array compression + argsort permutation
    a = argsort_permutation(compress(a).compressed)
    q, r = divmod(k, n)
    count = [q] * n
    for i in a[:r]:
        count[i] += 1
    print(*count, sep="\n")


main()
