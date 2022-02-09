import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:], nb.i8), cache=True)
def solve(
  n: int,
  a: np.ndarray,
  t: int,
) -> typing.NoReturn:
  a = np.hstack((
    np.array([0]),
    a,
    np.array([t]),
  ))
  m = len(a)
  for i in range(m - 1, 0, -1):
    a[i] -= a[i - 1]
  a[1::2] *= -1
  a[0] = n
  for i in range(m - 1):
    a[i + 1] = min(a[i + 1] + a[i], n)
  print('Yes' if np.all(a > 0) else 'No')


def main() -> typing.NoReturn:
  n, m, t = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(n, a, t)


main()
