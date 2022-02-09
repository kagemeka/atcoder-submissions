import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    n = len(a)
    prev = np.empty(n, np.int64)
    last = np.full(26, -1, np.int64)
    for i in range(n):
        prev[i] = last[a[i]]
        last[a[i]] = i
    mod = 10 ** 9 + 7

    dp = np.zeros(n + 2, np.int64)
    for i in range(2, n + 2):
        j = prev[i - 2]
        dp[i] = dp[i - 2] - dp[j] + (j == -1)
        dp[i] = (dp[i] + dp[i - 1]) % mod
    print(dp[-1])

def main() -> typing.NoReturn:
    a = np.array([ord(x) - 97 for x in input()])
    solve(a)


main()
