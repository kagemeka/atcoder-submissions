import typing
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  mod = 998_244_353
  m = 1 << 13
  n = a.size
  idx = np.argsort(a)
  a, b = a[idx], b[idx]

  dp = np.zeros((n + 1, m, 2), dtype=np.int64)
  dp[0, 0, 0] = 1
  s = 0
  for i in range(n):
    x, y = a[i], b[i]
    for j in range(m):
      dp[i + 1, j, 0] = dp[i, j, 0] + dp[i, j, 1]
      if j - y >= 0:
        dp[i + 1, j, 1] = dp[i, j - y, 0] + dp[i, j - y, 1]
    dp[i + 1] %= mod
    s += dp[i + 1, :x + 1, 1].sum() % mod
  print(s % mod)



def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n)
  solve(a, b)


main()
