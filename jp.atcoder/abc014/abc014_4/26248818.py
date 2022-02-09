import typing
import sys
import numpy as np
import numba as nb

@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while 1 << l <= n: l += 1
  return l



@nb.njit
def tree_bfs(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  parent = np.full(n, -1, np.int32)
  depth = np.zeros(n, np.int32)
  fifo_que = [root]
  for u in fifo_que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      fifo_que.append(v)
  return parent, depth


@nb.njit
def lca_preprocess(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> np.ndarray:
  parent, depth = tree_bfs(n, g, edge_idx, root)
  k = bit_length(depth.max())
  ancestors = np.empty((k, n), np.int32)
  ancestors[0] = parent.copy()
  ancestors[0, root] = root
  for i in range(k - 1):
    ancestors[i + 1] = ancestors[i][ancestors[i]]
  return depth, ancestors


@nb.njit
def lca(
  depth: np.ndarray,
  ancestors: np.ndarray,
  u: int,
  v: int,
) -> int:
  if depth[u] > depth[v]: u, v = v, u
  d = depth[v] - depth[u]
  for i in range(bit_length(d)):
    if d >> i & 1: v = ancestors[i, v]
  if v == u: return u
  for i in range(len(ancestors) - 1, -1, -1):
    nu, nv = ancestors[i, u], ancestors[i, v]
    if nu == nv: continue
    u, v = nu, nv
  return ancestors[0, u]



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
  depth, ancestors = lca_preprocess(n, g, edge_idx, 0)

  def dist(u, v):
    l = lca(depth, ancestors, u, v)
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
