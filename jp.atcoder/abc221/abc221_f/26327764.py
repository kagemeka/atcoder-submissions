import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def double_tree(g: np.ndarray) -> np.ndarray:
  n = g.max() + 1
  assert len(g) == n - 1
  t = np.empty(((n - 1) * 2, 2), np.int64)
  add_idx = 0
  def add_edge(u, v):
    nonlocal add_idx
    t[add_idx] = (u, v)
    add_idx += 1

  for i in range(len(g)):
    u, v = g[i]
    add_edge(u, n + i)
    add_edge(v, n + i)
  return t


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
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx


@nb.njit
def euler_tour_edge(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
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


@nb.njit
def euler_tour_node(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[(np.ndarray, ) * 4]:
  tour, parent, depth = euler_tour_edge(g, edge_idx, root)
  n = len(tour) >> 1
  first_idx = np.full(n, -1, np.int64)
  for i in range(n << 1):
    u = tour[i]
    if u < 0:
      tour[i] = parent[~u]
      continue
    first_idx[u] = i
  return tour[:-1], first_idx, parent, depth


@nb.njit
def tree_bfs(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  fifo_que = [root]
  for u in fifo_que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      fifo_que.append(v)
  return parent, depth


@nb.njit
def tree_diameter_path(
  g: np.ndarray,
  edge_idx: np.ndarray,
) -> np.ndarray:
  _, depth = tree_bfs(g, edge_idx, 0)
  parent, depth = tree_bfs(g, edge_idx, np.argmax(depth))
  u = np.argmax(depth)
  d = depth[u]
  path = np.empty(d + 1, np.int64)
  for i in range(d + 1):
    path[i] = u
    u = parent[u]
  return path


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(uv: np.ndarray) -> typing.NoReturn:
  n = len(uv) + 1
  g = double_tree(uv)
  n += n - 1
  g = csgraph_to_directed(g)
  g, edge_idx, _ = sort_csgraph(n, g)
  path = tree_diameter_path(g, edge_idx)
  diameter = len(path) - 1
  radius = diameter >> 1
  root = path[radius]
  tour, _, _, depth = euler_tour_node(g, edge_idx, root)

  mod = 998_244_353
  s = 1
  tot = 0
  cnt = 0
  for u in tour:
    if u == root:
      s *= cnt + 1
      s %= mod
      tot += cnt
      cnt = 0
      continue
    cnt += depth[u] == radius

  s -= tot + 1
  print(s % mod)



def main() -> typing.NoReturn:
  n = int(input())
  uv = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  solve(uv)


main()
