import typing
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def floyd_warshall(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert inf > g.max() * n
  dist = np.full((n, n), inf, np.int64)
  for i in range(n): dist[i, i] = 0
  for u in range(n):
    for v in range(n):
      if g[u, v] == 0: continue
      dist[u, v] = g[u, v]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist


@nb.njit(
  (nb.i8[:, :], nb.i8),
  cache=True,
)
def csgraph_to_dense(
  csgraph: np.ndarray,
  n: int,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  g = np.zeros((n, n), np.int64)
  for i in range(m):
    u, v, w = csgraph[i]
    g[u, v] = g[v, u] = w
  return g


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  g: np.ndarray,
) -> typing.NoReturn:
  g = csgraph_to_dense(g, n)
  dist = floyd_warshall(g)
  res = 1 << 60
  for i in range(n):
    res = min(res, dist[i].max())
  print(res)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abt = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abt[:, :2] -= 1
  solve(n, abt)


main()
