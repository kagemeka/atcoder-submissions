import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx



@nb.njit
def csgraph_is_sorted(g: np.ndarray) -> bool:
  return np.all(g[1:, 0] >= g[:-1, 0])


# csgraph
@nb.njit
def graph_bfs(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph_is_sorted(g)
  level = np.full(n, -1, np.int64)
  level[src] = 0
  que = [src]
  for u in que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      if level[v] != -1: continue
      level[v] = level[u] + 1
      que.append(v)
  return level



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, ab: np.ndarray) -> typing.NoReturn:
  g, edge_idx, _ = sort_csgraph(n, ab)

  cnt = 0
  for i in range(n):
    level = graph_bfs(n, g, edge_idx, i)
    cnt += np.count_nonzero(level != -1)
  print(cnt)



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, ab)


main()
