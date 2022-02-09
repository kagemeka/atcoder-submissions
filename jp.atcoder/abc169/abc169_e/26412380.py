import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
  n = len(ab)
  a, b = ab[:, 0], ab[:, 1]
  a.sort()
  b.sort()
  if n & 1:
    s = b[n >> 1] - a[n >> 1] + 1
  else:
    s = b[n >> 1] + b[(n >> 1) - 1]
    s -= a[n >> 1] + a[(n >> 1) - 1]
    s += 1
  print(s)


def main() -> typing.NoReturn:
  n = int(input())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab)



main()
