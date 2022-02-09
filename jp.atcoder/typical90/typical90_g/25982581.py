import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ) * 2, cache=True)
def solve(a: np.ndarray, b: np.ndarray) -> typing.NoReturn:
  inf = 1 << 60
  a = np.hstack((
    np.array([-inf, inf]),
    a,
  ))
  a.sort()
  d0 = np.abs(a[np.searchsorted(a, b, side='left')] - b)
  d1 = np.abs(a[np.searchsorted(a, b, side='right') - 1] - b)
  for i in range(b.size):
    print(min(d0[i], d1[i]))




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  q = int(input())
  b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a, b)


main()
