import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], nb.i8, nb.i8), cache=True)
def solve(
  ab: np.ndarray,
  x: int,
  y: int,
) -> typing.NoReturn:
  n = len(ab)

  inf = 1 << 60
  dp = np.full((x + 1, y + 1), inf, np.int64)
  dp[0, 0] = 0
  for i in range(n):
    a, b = ab[i]
    ndp = dp.copy()
    for j in range(x + 1):
      for k in range(y + 1):
        ndp[min(j + a, x), min(k + b, y)] = min(
          ndp[min(j + a, x), min(k + b, y)],
          dp[j, k] + 1,
        )
    dp = ndp
  print(-1 if dp[x, y] == inf else dp[x, y])




def main() -> typing.NoReturn:
  n = int(input())
  x, y = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab, x, y)



main()
