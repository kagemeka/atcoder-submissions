import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, b: np.ndarray) -> typing.NoReturn:
  n = len(a)
  mod = 998_244_353

  m = 1 << 12
  dp = np.zeros(m, np.int64)
  dp[0] = 1
  for i in range(n):
    ndp = np.zeros(m, np.int64)
    dp = dp.cumsum()
    dp %= mod
    dp[:a[i]] = 0
    dp[b[i] + 1:] = 0
  print(dp.sum() % mod)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, b)


main()
