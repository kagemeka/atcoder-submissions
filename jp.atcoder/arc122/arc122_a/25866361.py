import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  mod = 10 ** 9 + 7
  dp = np.zeros((n, 2), np.int64)
  dp[0, 1] = 1
  for i in range(n - 1):
    dp[i + 1, 1] = dp[i].sum() % mod
    dp[i + 1, 0] = dp[i, 1]

  s = a[0] * dp[n - 1].sum() % mod
  for i in range(1, n):
    l = i - 1
    r = n - 1 - i
    s += a[i] * dp[l].sum() % mod * dp[r].sum() % mod
    s += -a[i] * dp[l, 1] % mod * dp[r, 1] % mod
    s %= mod
  print(s)



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
