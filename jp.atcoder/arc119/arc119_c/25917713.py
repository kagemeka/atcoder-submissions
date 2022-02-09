import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  a[1::2] *= -1
  a = a.cumsum()
  cnt = np.count_nonzero(a == 0)
  a = np.searchsorted(np.unique(a), a)
  b = np.bincount(a)
  cnt += np.sum(b * (b - 1) // 2)
  print(cnt)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
