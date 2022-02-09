import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def cross(x0: int, y0: int, x1: int, y1: int) -> int:
  return x0 * y1 - x1 * y0


@nb.njit((nb.i8, ) * 4 + (nb.i8[:, :], ), cache=True)
def solve(
  x0: int,
  y0: int,
  x1: int,
  y1: int,
  xy: np.ndarray,
) -> typing.NoReturn:
  n = len(xy)
  xy = np.vstack((xy, xy[:1]))
  x, y = xy[:, 0], xy[:, 1]
  x2, y2 = x[:-1], y[:-1]
  x3, y3 = x[1:], y[1:]
  p0 = cross(x1 - x0, y1 - y0, x2 - x0, y2 - y0)
  p0 *= cross(x1 - x0, y1 - y0, x3 - x0, y3 - y0)
  p1 = cross(x0 - x2, y0 - y2, x3 - x2, y3 - y2)
  p1 *= cross(x1 - x2, y1 - y2, x3 - x2, y3 - y2)
  cnt = 1 + np.count_nonzero((p0 < 0) & (p1 < 0)) // 2
  print(cnt)



def main() -> typing.NoReturn:
  x0, y0, x1, y1 = map(int, input().split())
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(x0, y0, x1, y1, xy)


main()
