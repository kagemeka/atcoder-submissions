import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, b: np.ndarray) -> typing.NoReturn:
  n = len(a)
  sort_idx = np.argsort(a)
  a, b = a[sort_idx], b[sort_idx]
  m = 1 << 16
  dp = np.zeros(m, np.int64)
  dp[0] = 1
  mod = 998_244_353
  cnt = 0
  for i in range(n):
    if a[i] >= b[i]:
      cnt += dp[0:a[i] - b[i] + 1].sum() % mod
    for j in range(m - 1, b[i] - 1, -1):
      dp[j] += dp[j - b[i]]
      dp[j] %= mod

  print(cnt % mod)




def main() -> typing.NoReturn:
  n = int(input())
  a = np .array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np .array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, b)


main()
