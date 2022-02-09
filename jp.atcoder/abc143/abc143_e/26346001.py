import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit
def shortest_dist_floyd_warshall(g: np.ndarray) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  g = g.copy()
  for i in range(n): g[i, i] = 0
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
  return g


@nb.njit((nb.i8, nb.i8, nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(
  n: int,
  l: int,
  abc: np.ndarray,
  st: np.ndarray,
) -> typing.NoReturn:
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  for i in range(len(abc)):
    a, b, c = abc[i]
    g[a, b] = g[b, a] = c
  for i in range(n): g[i, i] = 0

  g = shortest_dist_floyd_warshall(g)
  for i in range(n):
    for j in range(n):
      g[i, j] = 1 if g[i, j] <= l else inf
  g = shortest_dist_floyd_warshall(g)
  for i in range(len(st)):
    s, t = st[i]
    print(-1 if g[s, t] == inf else g[s, t] - 1)





def main() -> typing.NoReturn:
  n, m, l = map(int, input().split())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  abc = I[:m * 3].reshape(m, 3)
  abc[:, :2] -= 1
  st = I[m * 3 + 1:].reshape(-1, 2) - 1
  solve(n, l, abc, st)


main()
