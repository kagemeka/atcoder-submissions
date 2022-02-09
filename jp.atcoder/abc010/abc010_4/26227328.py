import typing
import sys
import numpy as np
import numba as nb


# dense graph $O(V^2)$
@nb.njit
def maximum_flow_dinic(
  g: np.ndarray,
  src: int,
  sink: int,
) -> int:
  n = len(g)
  inf = 1 << 60
  level = np.full(n, -1, np.int32)

  def _update_level():
    level[:] = -1
    level[src] = 0
    fifo_que = [src]
    for u in fifo_que:
      for v in range(n):
        if level[v] != -1 or g[u, v] <= 0: continue
        level[v] = level[u] + 1
        fifo_que.append(v)

  flow_in = np.zeros(n + 1, np.int64)
  flow_out = np.zeros(n + 1, np.int64)
  prev = np.full(n, -1, np.int64)

  def _compute_flow():
    flow_in[:] = 0
    flow_in[src] = inf
    flow_out[:] = 0
    prev[:] = -1
    st = [src]
    while st:
      u = st.pop()
      if u < 0:
        u = -u - 1
        if u == src: return flow_out[src]
        p = prev[u]
        f = flow_out[u]
        flow_out[p] += f
        flow_in[p] -= f
        g[p, u] -= f
        g[u, p] += f
        flow_in[u] = flow_out[u] = 0
        continue
      st.append(-u - 1)
      p = prev[u]
      if u != src:
        flow_in[u] = min(flow_in[p], g[p, u])
      if u == sink:
        flow_out[u] = flow_in[u]
        continue
      if flow_in[u] == 0: continue
      for v in range(n):
        if g[u, v] == 0 or level[v] <= level[u]: continue
        prev[v] = u
        st.append(v)

  flow = 0
  while 1:
    _update_level()
    if level[sink] == -1: return flow
    flow += _compute_flow()






@nb.njit((nb.i8, nb.i8[:], nb.i8[:, :]), cache=True)
def solve(
  n: int,
  p: np.ndarray,
  ab: np.ndarray,
) -> typing.NoReturn:
  n += 1
  g = np.zeros((n, n), np.int64)
  for i in range(len(ab)):
    a, b = ab[i]
    g[a, b] = g[b, a] = 1
  for i in p: g[i, n - 1] = 1
  v = maximum_flow_dinic(g, 0, n - 1)
  print(v)




def main() -> typing.NoReturn:
  n, g, e = map(int, input().split())
  p = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(e, 2)
  solve(n, p, ab)


main()
