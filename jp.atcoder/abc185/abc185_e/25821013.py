import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(
  a: np.ndarray,
  b: np.ndarray,
) -> typing.NoReturn:
  n, m = a.size, b.size

  cost = np.empty((n + 1, m + 1), np.int64)
  cost[0] = np.arange(m + 1)
  cost[:, 0] = np.arange(n + 1)

  for i in range(n):
    for j in range(m):
      cost[i + 1][j + 1] = min(
        cost[i + 1][j] + 1,
        cost[i][j + 1] + 1,
        cost[i][j] + (a[i] != b[j]),
      )

  print(cost[n][m])


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
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
