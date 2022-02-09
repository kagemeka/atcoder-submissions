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

  dp = np.zeros(m, dtype=np.int64)
  s = 0
  dp[0] = 1
  for i in range(n):
    x, y = a[i], b[i]
    s += dp[:max(x - y + 1, 0)].sum()
    dp[::-1][:-y] += dp[::-1][y:]
    dp %= mod
  print(s % mod)


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n)
  solve(a, b)


main()
