import sys
import typing

import numba as nb
import numpy as np


@nb.njit((nb.i8[:], ) * 2, cache=True)
def solve(a: np.ndarray, b: np.ndarray) -> typing.NoReturn:
  a.sort()
  b.sort()
  e = np.abs(b - a)
  print(e.sum())


def main() -> typing.NoReturn:
  n = int(input())
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
