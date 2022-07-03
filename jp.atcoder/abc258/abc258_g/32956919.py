# / mypy: ignore-errors
import typing


def popcount(n: int) -> int:
    M0 = 0x5555555555555555
    M1 = 0x3333333333333333
    M2 = 0x0F0F0F0F0F0F0F0F
    n -= (n >> 1) & M0
    n = (n & M1) + ((n >> 2) & M1)
    n = (n + (n >> 4)) & M2
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x7F


# n >= 2^63 is arbitraty precition integer and slow in Python.


N = 63


def main() -> None:
    n = int(input())
    a = [[] for _ in range(n)]
    for i in range(n):
        s = input()
        for j in range(0, n, N):
            a[i].append(int(s[j : j + N][::-1], 2))
    cnt = 0
    for i in range(n):
        for j in range(i):
            if not a[i][j // N] >> (j & (N - 1)) & 1:
                continue
            cnt += sum(popcount(x & y) for x, y in zip(a[i], a[j]))
    print(cnt // 3)


main()
