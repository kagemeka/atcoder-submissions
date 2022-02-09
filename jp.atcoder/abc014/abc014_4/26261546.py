import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def euler_tour(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int32)
  depth = np.zeros(n, np.int32)
  tour = np.empty(n * 2, np.int32)
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
def bit_length_table(n: int) -> np.ndarray:
  l = np.zeros(n, np.int64)
  for i in range(1, n): l[i] = l[i >> 1] + 1
  return l



S = typing.TypeVar('S')
@nb.njit
def sparse_table_build(
  bit_len: np.ndarray,
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  k = bit_len[n]
  table = np.empty((k, ) + a.shape, np.int64)
  table[0] = a.copy()
  for i in range(k - 1):
    table[i + 1] = table[i].copy()
    for j in range(n - (1 << i)):
      table[i + 1, j] = op(table[i, j], table[i, j + (1 << i)])
  return table


@nb.njit
def sparse_table_get(
  bit_len: np.ndarray,
  table: np.ndarray,
  op: typing.Callable[[S, S], S],
  l: int,
  r: int,
) -> S:
  k = bit_len[r - l] - 1
  return op(table[k, l], table[k, r - (1 << k)])



@nb.njit
def sparse_table_op(x: S, y: S) -> S:
  return x if x[0] <= y[0] else y



@nb.njit
def lca_preprocess(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> np.ndarray:
  tour, parent, depth = euler_tour(g, edge_idx, root)
  for i in range(n * 2):
    if tour[i] < 0: tour[i] = parent[~tour[i]]
  tour = tour[:-1]
  first_idx = np.full(n, -1, np.int32)
  for i in range(n * 2 - 1):
    u = tour[i]
    if first_idx[u] != -1: continue
    first_idx[u] = i
  a = np.empty((len(tour), 2), np.int64)
  a[:, 0], a[:, 1] = depth[tour], tour
  bit_len = bit_length_table(n * 2)
  table = sparse_table_build(bit_len, sparse_table_op, a)
  return first_idx, table, bit_len



@nb.njit
def lca(
  first_idx: np.ndarray,
  sparse_table: np.ndarray,
  bit_len,
  u: int,
  v: int,
) -> int:
  l, r = first_idx[u], first_idx[v]
  if l > r: l, r = r, l
  return sparse_table_get(
    bit_len, sparse_table, sparse_table_op,
    l, r,
  )[1]



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



@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(xy: np.ndarray, ab: np.ndarray) -> typing.NoReturn:
  n = len(xy) + 1
  g = csgraph_to_directed(xy)
  g, edge_idx, _ = sort_csgraph(n, g)
  first_idx, table, bit_len = lca_preprocess(n, g, edge_idx, 0)
  _, _, depth = euler_tour(g, edge_idx, 0)

  def dist(u, v):
    l = lca(first_idx, table, bit_len, u, v)
    return depth[u] + depth[v] - 2 * depth[l]

  for i in range(len(ab)):
    a, b = ab[i]
    print(dist(a, b) + 1)



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
