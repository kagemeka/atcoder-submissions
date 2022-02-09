import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ) * 3, cache=True)
def solve(
  a: np.ndarray,
  b: np.ndarray,
  c: np.ndarray,
) -> typing.NoReturn:
  n = len(a)
  s = b[0]
  for i in range(1, n):
    s += b[i]
    if a[i] == a[i - 1] + 1: s += c[a[i - 1]]
  print(s)


def main() -> typing.NoReturn:
  n = int(input().rstrip())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, b, c)


main()
