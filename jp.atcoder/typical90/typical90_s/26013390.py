import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  inf = 1 << 60
  dp = np.full((n, n), inf, np.int64)
  for i in range(n - 1):
    dp[i, i + 1] = np.abs(a[i] - a[i + 1])

  for d in range(2, n):
    for l in range(n - d):
      r = l + d
      dp[l, r] = dp[l + 1, r - 1] + np.abs(a[l] - a[r])
      for m in range(l + 1, r - 1):
        dp[l, r] = min(
          dp[l, r],
          dp[l, m] + dp[m + 1, r],
        )


  print(dp[0, -1])



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
