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
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx



@nb.njit
def csgraph_to_undirected(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def connected_components_dfs(n: int, g: np.ndarray):
  g = csgraph_to_undirected(g)
  g, edge_idx, _ = sort_csgraph(n, g)
  label = np.full(n, -1, np.int64)
  l = 0
  for i in range(n):
    if label[i] != -1: continue
    label[i] = l
    st = [i]
    while st:
      u = st.pop()
      for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
        if label[v] != -1: continue
        label[v] = l
        st.append(v)
    l += 1
  return label




@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = a.size
  a = np.searchsorted(np.unique(a), a)
  m = a.max() + 1
  g = np.empty((n, 2), np.int64)
  idx_to_add = 0
  def add_edge(u, v):
    nonlocal idx_to_add
    g[idx_to_add] = (u, v)
    idx_to_add += 1

  for i in range(n // 2):
    x, y = a[i], a[n - 1 - i]
    add_edge(x, y)
    add_edge(y, x)

  g = g[:idx_to_add]
  label = connected_components_dfs(m, g)
  print(m - label.max() - 1)





def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
