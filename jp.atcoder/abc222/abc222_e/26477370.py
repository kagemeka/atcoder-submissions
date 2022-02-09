import typing
import sys
import numpy as np
import numba as nb





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
def dfs_path(
  g: np.ndarray,
  edge_idx: np.ndarray,
  src: int,
  dst: int,
) -> np.ndarray:
  _, parent, depth = euler_tour_edge(g, edge_idx, src)
  u = dst
  d = depth[u]
  path = np.empty(d + 1, np.int64)
  for i in range(d + 1):
    path[-1 - i] = u
    u = parent[u]
  return path



@nb.njit
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  idx = g[:, 0] << 31 | g[:, 1]
  sort_idx = np.argsort(idx, kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit((nb.i8[:], nb.i8[:, :], nb.i8), cache=True)
def solve(
  a: np.ndarray,
  uv: np.ndarray,
  k: int,
) -> typing.NoReturn:
  n, m = len(uv) + 1, len(a)

  mod = 998_244_353
  g = csgraph_to_directed(uv)
  g, edge_idx, _ = sort_csgraph(n, g)

  cnt = np.zeros((n, n), np.int64)
  total_edge_cnt = 0
  for i in range(m - 1):
    path = dfs_path(g, edge_idx, a[i], a[i + 1])
    for j in range(len(path) - 1):
      cnt[path[j], path[j + 1]] += 1
    total_edge_cnt += len(path) - 1

  if total_edge_cnt + k < 0 or (total_edge_cnt + k) & 1:
    print(0)
    return

  not_used_cnt = 0
  for i in range(len(g)):
    u, v = g[i]
    not_used_cnt += cnt[u, v] == cnt[v, u] == 0

  not_used_cnt //= 2

  r = (k + total_edge_cnt) // 2

  b = np.zeros(n * n, np.int64)
  ptr = 0
  for i in range(n - 1):
    for j in range(i + 1, n):
      s = cnt[i, j] + cnt[j, i]
      if s == 0: continue
      b[ptr] = s
      ptr += 1
  b = b[:ptr]

  assert r >= 0
  dp = np.zeros(r + 1, np.int64)
  dp[0] = 1
  for x in b:
    for j in range(r, x - 1, -1):
      dp[j] += dp[j - x]
      dp[j] %= mod
  ans = dp[r] * mod_pow(2, not_used_cnt, mod) % mod
  print(ans)


def main() -> typing.NoReturn:
  n, m, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  uv = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  solve(a, uv, k)


main()
