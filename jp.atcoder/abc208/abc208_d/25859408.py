import typing
import numpy as np
import sys
import numba as nb



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, abc: np.ndarray) -> typing.NoReturn:
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  m = len(abc)
  for i in range(m):
    a, b, c = abc[i]
    g[a, b] = c
  for i in range(n):
    g[i, i] = 0

  s = 0
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
    s += np.sum(g * (g != inf))
  print(s)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abc[:, :2] -= 1
  solve(n, abc)



main()
