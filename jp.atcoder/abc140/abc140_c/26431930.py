import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(b: np.ndarray) -> typing.NoReturn:
  n = len(b) + 1
  s = b[0] + b[-1]
  for i in range(n - 2):
    s += min(b[i], b[i + 1])
  print(s)


def main() -> typing.NoReturn:
  n = int(input())
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(b)


main()
