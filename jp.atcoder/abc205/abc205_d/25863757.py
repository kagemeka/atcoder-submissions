import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, k: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(k)
  b = a - np.arange(n)
  a = np.hstack((np.array([0]), a))
  b = np.hstack((np.array([1]), b))
  i = np.searchsorted(b, k, side='right') - 1
  res = a[i] + 1 + k - b[i]
  for x in res:
    print(x)


def main() -> typing.NoReturn:
  n, q = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  k = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
