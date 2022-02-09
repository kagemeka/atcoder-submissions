import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
  x, y = xy.T
  x.sort()
  y.sort()
  cand = np.array([
    x[-1] - x[0],
    x[-2] - x[0],
    x[-1] - x[1],
    y[-1] - y[0],
    y[-2] - y[0],
    y[-1] - y[1],
  ])
  cand.sort()
  print(cand[-2])


def main() -> typing.NoReturn:
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy)


main()
