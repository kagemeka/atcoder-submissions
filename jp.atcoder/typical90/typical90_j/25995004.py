import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ) * 2, cache=True)
def solve(cp: np.ndarray, lr: np.ndarray) -> typing.NoReturn:
  n = len(cp)
  c, p = cp[:, 0], cp[:, 1]
  p1 = np.zeros(n + 1, np.int64)
  p2 = np.zeros(n + 1, np.int64)
  p1[1:][c == 1] = p[c == 1]
  p2[1:][c == 2] = p[c == 2]
  p1 = p1.cumsum()
  p2 = p2.cumsum()
  for i in range(len(lr)):
    l, r = lr[i]
    s1 = p1[r] - p1[l - 1]
    s2 = p2[r] - p2[l - 1]
    print(s1, s2)


def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  cp = I[:2 * n].reshape(n, 2)
  lr = I[2 * n + 1:].reshape(-1, 2)
  solve(cp, lr)


main()
