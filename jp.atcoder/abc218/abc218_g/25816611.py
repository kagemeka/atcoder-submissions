import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:, :], ), cache=True)
def sort_csgraph(
  n: int,
  csgraph: np.ndarray,
) -> typing.Tuple[
  np.ndarray,
  np.ndarray,
  np.ndarray,
]:
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  original_idx = np.arange(len(csgraph))[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))
  return csgraph, edge_idx, original_idx



@nb.njit
def fw_build(n: int) -> np.ndarray:
  return np.zeros(n + 1, np.int64)


@nb.njit
def fw_build_from_array(a: np.ndarray) -> np.ndarray:
  assert a[0] == 0
  fw = a.copy()
  n = len(fw)
  for i in range(n):
    j = i + (i & -i)
    if j < n: fw[j] += fw[i]
  return fw


@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] += x
    i += i & -i


@nb.njit
def fw_get(fw: np.ndarray, i: int) -> int:
  v = 0
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v


@nb.njit
def fw_lower_bound(fw: np.ndarray, x: int) -> int:
  n = len(fw)
  l = 1
  while l << 1 < n: l <<= 1
  v = 0
  i = 0
  while l:
    if i + l < n and v + fw[i + l] < x:
      i += l
      v += fw[i]
    l >>= 1
  return i + 1


@nb.njit
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v



@nb.njit
def csgraph_to_undirected(csgraph: np.ndarray) -> np.ndarray:
  m = len(csgraph)
  csgraph = np.vstack((csgraph, csgraph))
  csgraph[m:, :2] = csgraph[m:, 1::-1]
  return csgraph



@nb.njit
def euler_tour(
  n: int,
  csgraph: np.ndarray,
  root: int,
) -> typing.Tuple[
  np.ndarray,
  np.ndarray,
  np.ndarray,
]:
  assert len(csgraph) == n - 1
  csgraph = csgraph_to_undirected(csgraph)
  csgraph, edge_idx, _ = sort_csgraph(n, csgraph)
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n * 2, np.int64)
  visited = np.zeros(n, np.bool8)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if visited[u]: continue
    visited[u] = True
    st.append(u)
    for v in csgraph[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth



@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(
  a: np.ndarray,
  uv: np.ndarray,
) -> typing.NoReturn:
  n = len(a)
  a, retrieve = compress_array(a)

  tour, parent, depth = euler_tour(n, uv, 0)
  median = np.empty(n, np.int64)

  def compute_medians():
    mx = a.max()
    fw = fw_build(mx + 1)
    visited = np.zeros(n, np.bool8)
    for u in tour[:-1]:
      if visited[u]:
        fw_set(fw, a[-u] + 1, -1)
        continue
      visited[u] = True
      fw_set(fw, a[u] + 1, 1)
      cnt = fw_get(fw, mx + 1)
      l = fw_lower_bound(fw, (cnt + 1) // 2) - 1
      r = fw_lower_bound(fw, cnt // 2 + 1) - 1
      median[u] = (retrieve[l] + retrieve[r]) // 2

  compute_medians()


  uv = np.vstack((uv, uv[:, ::-1]))
  uv, edge_idx, _ = sort_csgraph(n, uv)
  res = np.empty(n, np.int64)
  for u in np.argsort(depth)[::-1]:
    is_taro_turn = depth[u] & 1 == 0
    v = uv[edge_idx[u]:edge_idx[u + 1], 1]
    v = v[v != parent[u]]
    if len(v) == 0:
      res[u] = median[u]
      continue
    res[u] = res[v].max() if is_taro_turn else res[v].min()

  print(res[0])



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  uv = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  solve(a, uv)


main()
