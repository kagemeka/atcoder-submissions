import sys
import typing

import numba as nb
import numpy as np


@nb.njit((nb.i8[:], ), cache=True)
def solve(
  a: np.ndarray,
) -> typing.NoReturn:
  n = a.size
  a.sort()
  s = a.cumsum()
  s = a[1:] * np.arange(1, n) - s[:-1]
  print(s.sum())



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
