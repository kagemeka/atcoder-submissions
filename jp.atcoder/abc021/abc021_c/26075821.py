import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def csgraph_to_undirected(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g



@nb.njit
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx


@nb.njit
def shortest_path_cnt_bfs(
  n: int,
  g: np.ndarray,
  src: int,
  mod: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  g, edge_idx, _ = sort_csgraph(n, g)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  paths = np.zeros(n, np.int64)
  paths[src] = 1
  fifo_que = [src]
  for u in fifo_que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      dv = dist[u] + 1
      if dv > dist[v]: continue
      if dv == dist[v]:
        paths[v] += paths[u]
        paths[v] %= mod
        continue
      dist[v] = dv
      paths[v] = paths[u]
      fifo_que.append(v)
  return dist, paths


@nb.njit((nb.i8, nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(
  n: int,
  a: int,
  b: int,
  xy: np.ndarray,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  m = len(xy)
  g = csgraph_to_undirected(xy)
  _, cnt = shortest_path_cnt_bfs(n, g, a, mod)
  print(cnt[b])

def main() -> typing.NoReturn:
  n = int(input())
  a, b = map(lambda x: int(x) - 1, input().split())
  m = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, a, b, xy)


main()
