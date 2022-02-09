import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g



@nb.njit
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx



@nb.njit
def euler_tour_edge(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n << 1, np.int64)
  st = [root]
  for i in range(n << 1):
    u = st.pop()
    tour[i] = u
    if u < 0: continue
    st.append(~u)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth



@nb.njit((nb.i8[:], ), cache=True)
def solve(b: np.ndarray) -> typing.NoReturn:
  n = len(b) + 1
  g = np.empty((n - 1, 2), np.int64)
  g[:, 0] = b
  g[:, 1] = np.arange(1, n)
  g = csgraph_to_directed(g)
  g, edge_idx, _ = sort_csgraph(n, g)
  tour, parent, _ = euler_tour_edge(g, edge_idx, 0)

  salary = np.ones(n, np.int64)
  for u in tour:
    if u >= 0: continue
    u = ~u
    cand = [0] * 0
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      if v == parent[u]: continue
      cand.append(salary[v])
    if not cand: continue
    salary[u] += max(cand) + min(cand)
  print(salary[0])




def main() -> typing.NoReturn:
  n = int(input())
  b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ) - 1
  solve(b)

main()
