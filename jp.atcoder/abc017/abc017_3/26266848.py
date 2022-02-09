import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def solve(lrs: np.ndarray, m: int) -> typing.NoReturn:
  a = np.zeros(1 << 17, np.int64)
  tot = 0
  for i in range(len(lrs)):
    l, r, s = lrs[i]
    a[l] += s
    a[r + 1] -= s
    tot += s
  a = a[:m].cumsum()
  print(tot - a.min())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrs = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 3)
  lrs[:, :2] -= 1
  solve(lrs, m)


main()
