import typing
import heapq
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
)
def shortest_path_dijkstra(
  n: int,
  edges: np.ndarray,
  src: int,
) -> np.ndarray:
  inf = 1 << 60
  edges = edges[np.argsort(edges[:, 0])]
  idx = np.searchsorted(edges[:, 0], np.arange(n + 1))
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for edge_idx in range(idx[u], idx[u + 1]):
      _, v, w = edges[edge_idx]
      dv = du + w
      if dv >= dist[v]: continue
      dist[v] = dv
      heapq.heappush(hq, (dv, v))
  return dist



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  lrx: np.ndarray,
) -> typing.NoReturn:
  m = len(lrx)
  edges = np.zeros((2 * n + m, 3), np.int64)
  lrx[:, -1] = lrx[:, 1] - lrx[:, 0] + 1 - lrx[:, -1]
  lrx[:, 0] -= 1
  edges[:m] = lrx
  edge_idx = m
  for i in range(n):
    edges[edge_idx] = (i, i + 1, 1)
    edge_idx += 1
    edges[edge_idx] = (i + 1, i, 0)
    edge_idx += 1
  sort_idx = np.argsort(edges[:, 0])
  edges = edges[sort_idx]
  b = shortest_path_dijkstra(n + 1, edges, 0)
  a = b[1:] - b[:-1] ^ 1
  return a


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  a = solve(n, lrx)
  print(*a)


main()
