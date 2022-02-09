import typing
import sys
import numpy as np
import numba as nb





@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def floyd_warshall(
  n: int,
  g: np.ndarray,
) -> np.ndarray:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  dist = np.full((n, n), inf, np.int64)
  for i in range(n): dist[i, i] = 0
  for i in range(m):
    u, v, w = g[i]
    dist[u, v] = min(dist[u, v], w)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def to_undirected(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, 3)
  g = np.vstack((g, g))
  g[n:, :2] = g[n:, 1::-1]
  return g



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  g: np.ndarray,
) -> typing.NoReturn:
  g = to_undirected(g)
  dist = floyd_warshall(n, g)
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
