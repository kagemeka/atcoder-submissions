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


K = 6
M = (1 << K) - 1


def main() -> None:
    n = int(input())
    a = [[] for _ in range(n)]
    for i in range(n):
        s = input()
        step = 1 << K
        for j in range(0, n, step):
            a[i].append(int(s[j : j + step][::-1], 2))
    cnt = 0
    for i in range(n):
        for j in range(i):
            if not a[i][j >> K] >> (j & K) & 1:
                continue
            # cnt += (a[i] & a[j]).popcount()
            cnt += sum(popcount(x & y) for x, y in zip(a[i], a[j]))
    print(cnt // 3)


main()
