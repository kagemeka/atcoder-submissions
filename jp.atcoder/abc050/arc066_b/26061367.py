import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7

  dp = np.zeros(3, np.int64)
  dp[0] = 1
  for i in range(60, -1, -1):
    flg = n >> i & 1
    ndp = np.zeros(3, np.int64)
    if flg:
      ndp[0] += dp[0]
      ndp[1] += dp[0] + dp[1]
      ndp[2] += dp[2] * 3 + dp[1] * 2
    else:
      ndp[0] += dp[0] + dp[1]
      ndp[1] += dp[1]
      ndp[2] += dp[2] * 3 + dp[1]
    dp = ndp % mod

  print(dp.sum() % mod)


def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


main()
