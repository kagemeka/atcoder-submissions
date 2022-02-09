import typing
import sys
import numpy as np
import numba as nb
import heapq



@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def shortest_dist_dijkstra(
  g: np.ndarray,
  src: int,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert g.max() <= inf
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for v in range(n):
      dv = du + g[u, v]
      if dv >= dist[v]: continue
      dist[v] = dv
      heapq.heappush(hq, (dv, v))
  return dist


@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def shortest_path_dijkstra(
  g: np.ndarray,
  src: int,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert g.max() <= inf
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for v in range(n):
      dv = du + g[u, v]
      if dv >= dist[v]: continue
      dist[v] = dv
      predecessor[v] = u
      heapq.heappush(hq, (dv, v))
  return predecessor


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(
  n: int,
  st: np.ndarray,
) -> typing.NoReturn:
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  m = len(st)
  for i in range(m):
    s, t = st[i]
    g[s, t] = 1

  predecessor = shortest_path_dijkstra(g, 0)
  d0 = shortest_dist_dijkstra(g, 0)[-1]
  if d0 == inf:
    for _ in range(m):
      print(-1)
    return

  for i in range(m):
    s, t = st[i]
    if predecessor[t] != s:
      print(d0)
      continue
    g[s, t] = inf
    d1 = shortest_dist_dijkstra(g, 0)[-1]
    print(d1 if d1 != inf else -1)
    g[s, t] = 1




def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  st = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, st)


main()
