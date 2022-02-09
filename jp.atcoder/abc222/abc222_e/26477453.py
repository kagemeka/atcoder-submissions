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
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  idx = g[:, 0] << 32 | g[:, 1]
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
  mod = 998_244_353
  n, m = len(uv) + 1, len(a)
  g = csgraph_to_directed(uv)
  g, edge_idx, _ = sort_csgraph(n, g)

  _, parent, depth = euler_tour_edge(g, edge_idx, 0)
  cnt = np.zeros(n, np.int64)
  for i in range(m - 1):
    u, v = a[i], a[i + 1]
    if depth[u] > depth[v]: u, v = v, u
    while depth[v] > depth[u]:
      cnt[v] += 1
      v = parent[v]
    while u != v:
      cnt[u] += 1
      cnt[v] += 1
      u, v = parent[u], parent[v]

  total_edge_cnt = cnt.sum()
  if total_edge_cnt + k < 0 or (total_edge_cnt + k) & 1:
    print(0)
    return

  r = (k + total_edge_cnt) // 2
  assert r >= 0
  b = cnt[cnt > 0]
  not_used_cnt = n - 1 - len(b)
  dp = np.zeros(r + 1, np.int64)
  dp[0] = 1
  for x in b:
    for j in range(r, x - 1, -1):
      dp[j] += dp[j - x]
      dp[j] %= mod
  ans = dp[r] * mod_pow(2, not_used_cnt, mod) % mod
  print(ans)


def main() -> typing.NoReturn:
  n, m, k = map(int, sys.stdin.buffer.readline().split())
  a = np.array(
    sys.stdin.buffer.readline().split(),
    dtype=np.int64,
  ) - 1
  uv = np.array(
    sys.stdin.buffer.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  solve(a, uv, k)


main()
