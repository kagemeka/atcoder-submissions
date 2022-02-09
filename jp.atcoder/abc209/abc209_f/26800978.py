import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(h: np.ndarray) -> typing.NoReturn:
    n = len(h)
    a = h[1:] > h[:-1]
    a = np.zeros(n - 1, np.bool8)
    for i in range(n - 1):
        a[i] = 1 if h[i + 1] > h[i] else -1 if h[i + 1] < h[i] else 0

    mod = 10 ** 9 + 7
    dp = np.zeros(n, np.int64)
    dp[0] = 1
    for i in range(1, n):
        ndp = np.zeros(n, np.int64)
        if h[i - 1] <= h[i]:
            s = 0
            for j in range(i):
                s += dp[j]
                s %= mod
                ndp[j + 1] += s
        if h[i - 1] >= h[i]:
            s = 0
            for j in range(i - 1, -1, -1):
                s += dp[j]
                s %= mod
                ndp[j] += s
        dp = ndp % mod
    print(dp.sum() % mod)

def main() -> typing.NoReturn:
    n = int(input())
    h = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    solve(h)


main()
