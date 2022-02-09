import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
  n = len(xy)
  cand = np.zeros(n, np.bool8)
  target = np.array([0, 1, -2, -1])
  idx = np.argsort(xy[:, 0])
  cand[idx[target]] = True
  idx = np.argsort(xy[:, 1])
  cand[idx[target]] = True
  xy = xy[np.flatnonzero(cand)]
  n = len(xy)
  res = np.empty(n * (n - 1) // 2, np.int64)
  add_idx = 0
  for i in range(n - 1):
    for j in range(i + 1, n):
      res[add_idx] = np.max(np.abs(xy[i] - xy[j]))
      add_idx += 1
  res.sort()
  print(res[-2])


def main() -> typing.NoReturn:
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy)


main()
