import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def shortest_dist_floyd_warshall(g: np.ndarray) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  g = g.copy()
  inf = 1 << 60
  assert inf >= g.max()
  for i in range(n): g[i, i] = 0
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
  return g


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, abt: np.ndarray) -> typing.NoReturn:
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  m = len(abt)
  for i in range(m):
    a, b, t = abt[i]
    g[a, b] = g[b, a] = t

  dist = shortest_dist_floyd_warshall(g)
  mn = inf
  for i in range(n):
    mn = min(mn, dist[i].max())
  print(mn)



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abt = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abt[:, :2] -= 1
  solve(n, abt)

main()
