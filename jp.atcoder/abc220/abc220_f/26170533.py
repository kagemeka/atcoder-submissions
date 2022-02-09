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
  size = np.ones(n, np.int64)
  dist_sum = np.zeros(n, np.int64)
  tour = np.empty(n * 2, np.int32)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if u < 0:
      u = -u - 1
      p = parent[u]
      if p == -1: continue
      size[p] += size[u]
      dist_sum[p] += dist_sum[u] + size[u]
      continue
    st.append(-u - 1)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth, size, dist_sum



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(uv: np.ndarray) -> typing.NoReturn:
  n = len(uv) + 1
  m = len(uv)
  g = np.vstack((uv, uv[:, ::-1]))
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  tour, parent, depth, size, dist_sum = euler_tour(g, edge_idx, 0)
  for u in tour:
    if u < 0: continue
    p = parent[u]
    if p == -1: continue
    dist_sum[u] = dist_sum[p] + size[p] - 2 * size[u]

  for d in dist_sum:
    print(d)




def main() -> typing.NoReturn:
  n = int(input())
  uv = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  solve(uv)


main()
