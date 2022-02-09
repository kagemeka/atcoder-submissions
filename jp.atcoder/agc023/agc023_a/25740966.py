import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(
  a: np.ndarray,
) -> typing.NoReturn:
  a = a.cumsum()
  s = (a == 0).astype(np.int64).sum()
  v = np.unique(a)
  a = np.searchsorted(v, a)
  c = np.bincount(a)
  s += np.sum(c * (c - 1) // 2)
  print(s)



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
