import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(t: np.ndarray, px: np.ndarray) -> typing.NoReturn:
  n, m = t.size, len(px)
  s = t.sum()

  for i in range(m):
    p, x = px[i]
    print(s + x - t[p])


def main() -> typing.NoReturn:
  n = int(input())
  t = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  m = int(input())
  px = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2)
  px[:, 0] -= 1
  solve(t, px)


main()
