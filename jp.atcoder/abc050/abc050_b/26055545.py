import typing
import sys
import numpy as np
import numba as nb


def solve(t: np.ndarray, px: np.ndarray) -> typing.NoReturn:
  n, m = t.size, len(px)
  p, x = px.T
  s = t.sum()
  res = s + x - t[p]
  print(*res)

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
