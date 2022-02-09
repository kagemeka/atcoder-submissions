import typing


def longest_increasing_sequence(
    a: typing.List[int],
) -> typing.List[int]:
    import bisect
    n = len(a)
    inf = 1 << 60
    lis = [inf] * n
    for x in a:
        lis[bisect.bisect_right(lis, x)] = x
    return lis[:bisect.bisect_left(lis, inf)]


def main() -> typing.NoReturn:
    n = int(input())
    a = [int(input()) for _ in range(n)]

    # if A_i < A_j, they can be painted with the same color,
    # <-> if A_i >= A_j, they should be pained with different colors.


    # decreasing sequence

    print(len(longest_increasing_sequence(a[::-1])))

main()
