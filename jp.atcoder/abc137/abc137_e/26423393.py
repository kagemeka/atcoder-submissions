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
def strongly_connected_components(
  n: int,
  g: np.ndarray,
) -> np.ndarray:
  def scc_dfs(n, g):
    g, edge_idx, _ = sort_csgraph(n, g)
    que = np.empty(n, np.int64)
    ptr = -1
    visited = np.zeros(n, np.bool8)
    for i in range(n):
      if visited[i]: continue
      st = [i]
      while st:
        u = st.pop()
        if u < 0:
          que[ptr] = ~u
          ptr -= 1
          continue
        if visited[u]: continue
        visited[u] = True
        st.append(~u)
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
          if not visited[v]: st.append(v)
    return que

  def scc_reverse_dfs(n, g, que):
    g[:, :2] = g[:, 1::-1]
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in que:
      if label[i] != -1: continue
      st = [i]
      label[i] = l
      while st:
        u = st.pop()
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
          if label[v] != -1: continue
          label[v] = l
          st.append(v)
      l += 1
    return label

  g = g.copy()
  que = scc_dfs(n, g)
  return scc_reverse_dfs(n, g, que)


@nb.njit
def shortest_path_bellman_ford(
  n: int,
  g: np.ndarray,
  src: int,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  for _ in range(n - 1):
    for i in range(m):
      u, v, w = g[i]
      if dist[u] + w >= dist[v]: continue
      dist[v] = dist[u] + w
      predecessor[v] = u
  for i in range(m):
    u, v, w = g[i]
    if dist[u] + w < dist[v]:
      raise Exception('Negative cycle found.')
  return dist, predecessor



@nb.njit((nb.i8, nb.i8[:, :], nb.i8), cache=True)
def solve(n: int, abc: np.ndarray, p: int) -> typing.NoReturn:
  g = abc.copy()
  g[:, 2] = p - g[:, 2]
  label = strongly_connected_components(
    n, np.vstack((g, np.array([[n - 1, 0, 0]]))),
  )
  m = len(g)
  on_path = np.zeros(m, np.bool8)
  l0 = label[0]
  for i in range(m):
    u, v, w = g[i]
    on_path[i] = label[u] == l0 and label[v] == l0
  g = g[on_path]
  try:
    dist, _ = shortest_path_bellman_ford(n, g, 0)
  except:
    print(-1)
    return
  print(max(0, -dist[-1]))


def main() -> typing.NoReturn:
  n, m, p = map(int, input().split())
  abc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abc[:, :2] -= 1
  solve(n, abc, p)


main()
