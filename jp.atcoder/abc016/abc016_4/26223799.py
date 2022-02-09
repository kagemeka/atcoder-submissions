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
  x1 -= x0
  y1 -= y0
  x -= x0
  y -= y0
  p = cross(x1, y1, x[:-1], y[:-1])
  p *= cross(x1, y1, x[1:], y[1:])
  cnt = 1 + np.count_nonzero(p < 0) // 2
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
