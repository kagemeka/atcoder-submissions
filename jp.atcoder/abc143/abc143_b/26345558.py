import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(d: np.ndarray) -> typing.NoReturn:
  n = len(d)
  s = d.cumsum()
  tot = 0
  for i in range(n - 1):
    tot += d[i] * (s[-1] - s[i])
  print(tot)


def main() -> typing.NoReturn:
  n = int(input())
  d = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(d)


main()
