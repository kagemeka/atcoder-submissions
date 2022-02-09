import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, ) * 4 + (nb.i8[:], ), cache=True)
def solve(
  t: int,
  l: int,
  x: int,
  y: int,
  e: np.ndarray,
) -> typing.NoReturn:
  theta = 2 * np.pi * e / t
  z0 = l / 2 * (1  - np.cos(theta))
  y0 = -l / 2 * np.sin(theta)
  dist = np.sqrt(x ** 2 + (y - y0) ** 2)
  rad = np.arctan2(z0, dist)
  deg = np.rad2deg(rad)

  for d in deg:
    print(d)


def main() -> typing.NoReturn:
  t = int(input())
  l, x, y = map(int, input().split())
  q = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )[1:]
  solve(t, l, x, y, q)

main()
