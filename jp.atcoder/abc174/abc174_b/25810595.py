import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def solve(
  xy: np.ndarray,
  d: np.ndarray,
) -> typing.NoReturn:
  x, y = xy.T
  ok = x * x + y * y <= d * d
  print(ok.astype(np.int64).sum())


def main() -> typing.NoReturn:
  n, d = map(int, input().split())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy, d)


main()
