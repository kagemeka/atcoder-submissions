import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], nb.i8, nb.i8), cache=True)
def solve(ab: np.ndarray, w: int, k: int) -> typing.NoReturn:
  n = len(ab)

  dp = np.zeros((k + 1, w + 1), np.int64)
  for i in range(n):
    a, b = ab[i]
    for j in range(k, 0, -1):
      for x in range(a, w + 1):
        dp[j, x] = max(dp[j, x], dp[j - 1, x - a] + b)
  print(dp[-1, -1])


def main() -> typing.NoReturn:
  w = int(input())
  n, k = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab, w, k)


main()
