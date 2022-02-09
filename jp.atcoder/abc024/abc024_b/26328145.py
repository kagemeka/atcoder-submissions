import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, t: int) -> typing.NoReturn:
  tot = 0
  n = len(a)
  for i in range(n - 1):
    tot += min(a[i + 1] - a[i], t)
  print(tot + t)


def main() -> typing.NoReturn:
  n, t = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a, t)


main()
