# / mypy: ignore-errors
import typing


# def popcount(n: int) -> int:
#     M0 = 0x5555555555555555
#     M1 = 0x3333333333333333
#     M2 = 0x0F0F0F0F0F0F0F0F
#     n -= (n >> 1) & M0
#     n = (n & M1) + ((n >> 2) & M1)
#     n = (n + (n >> 4)) & M2
#     n = n + (n >> 8)
#     n = n + (n >> 16)
#     n = n + (n >> 32)
#     return n & 0x7F


def popcount(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


N = 63


def main() -> None:
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        row = []
        for j in range(0, n, N):
            row.append(int(s[j : j + N][::-1], 2))
        a.append(row)
    cnt = 0
    for i in range(n):
        for j in range(i):
            if not a[i][j // N] >> (j % N) & 1:
                continue
            cnt += sum(popcount(x & y) for x, y in zip(a[i], a[j]))
    print(cnt // 3)


main()
