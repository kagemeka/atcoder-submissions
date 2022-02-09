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
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
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
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n * 2, np.int64)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if u < 0: continue
    st.append(-u - 1)
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
  tour = tour[:-1]
  first_idx = np.full(n, -1, np.int64)
  for i in range(2 * n - 1):
    u = tour[i]
    if u < 0:
      u = parent[~u]
      tour[i] = u
    if first_idx[u] == -1: first_idx[u] = i
  return tour, first_idx, parent, depth



@nb.njit
def uf_build(n: int) -> np.ndarray:
  return np.full(n, -1, np.int64)


@nb.njit
def uf_find(uf: np.ndarray, u: int) -> int:
  if uf[u] < 0: return u
  uf[u] = uf_find(uf, uf[u])
  return uf[u]


@nb.njit
def uf_unite(
  uf: np.ndarray,
  u: int,
  v: int,
) -> typing.NoReturn:
  u, v = uf_find(uf, u), uf_find(uf, v)
  if u == v: return
  if uf[u] > uf[v]: u, v = v, u
  uf[u] += uf[v]
  uf[v] = u



@nb.njit
def lca(
  g: np.ndarray,
  edge_idx: np.ndarray,
  vu: np.ndarray,
) -> np.ndarray:
  m = len(vu)
  tour, parent, _ = euler_tour_edge(g, edge_idx, 0)
  n = len(tour) >> 1
  first_idx = np.full(n, -1, np.int64)
  for i in range(len(tour)):
    u = tour[i]
    if u < 0: continue
    first_idx[u] = i

  for i in range(m):
    v, u = vu[i]
    if first_idx[v] < first_idx[u]: vu[i] = vu[i, ::-1]
  vu, query_idx, original_idx = sort_csgraph(n, vu)

  _lca = np.empty(m, np.int64)
  uf = uf_build(n)
  ancestor = np.arange(n)
  for v in tour[:-1]:
    if v >= 0: continue
    v = ~v
    for j in range(query_idx[v], query_idx[v + 1]):
      u = vu[j, 1]
      _lca[original_idx[j]] = ancestor[uf_find(uf, u)]
    p = parent[v]
    uf_unite(uf, v, p)
    ancestor[uf_find(uf, v)] = p
  _lca = np.zeros(m, np.int64)
  return _lca



@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(xy: np.ndarray, ab: np.ndarray) -> typing.NoReturn:
  n = len(xy) + 1
  g = csgraph_to_directed(xy)
  g, edge_idx, _ = sort_csgraph(n, g)
  _, _, depth = euler_tour_edge(g, edge_idx, 0)

  _lca = lca(g, edge_idx, ab)
  for i in range(len(ab)):
    u, v = ab[i]
    l = _lca[i]
    d = depth[u] + depth[v] - 2 * depth[l] + 1
    print(d)


def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  xy = I[:2 * (n - 1)].reshape(n - 1, 2) - 1
  ab = I[2 * n - 1:].reshape(-1, 2) - 1
  solve(xy, ab)


main()
