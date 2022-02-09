import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def maximum_flow_ford_fulkerson(
  g: np.ndarray,
  src: int,
  sink: int,
) -> int:
  n = len(g)
  inf = 1 << 60
  g = g.copy()
  prev = np.empty(n, np.int32)
  visited = np.zeros(n, np.bool8)

  def find_path():
    prev[:] = -1
    visited[:] = False
    st = [src]
    while st:
      u = st.pop()
      if u == sink: return
      if visited[u]: continue
      visited[u] = True
      for v in range(n - 1, -1, -1):
        if g[u, v] == 0 or visited[v]: continue
        prev[v] = u
        st.append(v)

  def compute_flow():
    v = sink
    flow = inf
    while prev[v] != -1:
      u = prev[v]
      flow = min(flow, g[u, v])
      v = u
    if flow == inf: return 0
    v = sink
    while prev[v] != -1:
      u = prev[v]
      g[u, v] -= flow
      g[v, u] += flow
      v = u
    return flow

  flow = 0
  while 1:
    find_path()
    f = compute_flow()
    if not f: return flow
    flow += f


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
  v = maximum_flow_ford_fulkerson(g, 0, n - 1)
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
