import typing


# def longest_increasing_sequence(
#     a: typing.List[int],
# ) -> typing.List[int]:
#     import bisect
#     n = len(a)
#     inf = 1 << 60
#     lis = [inf] * n
#     for x in a:



def main() -> typing.NoReturn:
    n = int(input())
    a = [int(input()) for _ in range(n)]

    # if A_i < A_j, they can be painted with the same color,
    # <-> if A_i >= A_j, they should be pained with different colors.


    # decreasing sequence

    cnt = 0
    mx = -1
    for x in a[::-1]:
        cnt += x >= mx
        mx = max(mx, x)
    print(cnt)

main()
