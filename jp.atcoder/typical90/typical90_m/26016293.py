import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx


@nb.njit((nb.i8[:, :], ), cache=True)
def csgraph_to_undirected(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit((nb.i8, nb.i8[:, :], nb.i8), cache=True)
def shortest_path_dijkstra(
  n: int,
  g: np.ndarray,
  src: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  assert g.shape == (len(g), 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  g = g[np.argsort(g[:, 0], kind='mergesort')]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = g[i]
      dv = du + w
      if dv >= dist[v]: continue
      dist[v] = dv
      predecessor[v] = u
      heapq.heappush(hq, (dv, v))
  return dist, predecessor



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, g: np.ndarray) -> typing.NoReturn:
  m = len(g)
  g = csgraph_to_undirected(g)
  dist0, _ = shortest_path_dijkstra(n, g, 0)
  dist1, _ = shortest_path_dijkstra(n, g, n - 1)
  for k in range(n):
    print(dist0[k] + dist1[k])


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  g = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  g[:, :2] -= 1
  solve(n, g)


main()
