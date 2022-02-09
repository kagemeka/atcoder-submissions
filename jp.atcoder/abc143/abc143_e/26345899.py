import typing
import sys
import numpy as np
import numba as nb
import heapq



@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g



@nb.njit((nb.i8, nb.i8, nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(
  n: int,
  l: int,
  abc: np.ndarray,
  st: np.ndarray,
) -> typing.NoReturn:
  inf = 1 << 60
  g = csgraph_to_directed(abc)
  g = g[np.argsort(g[:, 0], kind='mergesort')]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))

  def dijkstra(src):
    cnt = np.full(n, inf, np.int64)
    rem = np.zeros(n, np.int64)
    cnt[src] = 0
    rem[src] = l
    hq = [(0, -l, src)]

    while hq:
      cu, ru, u = heapq.heappop(hq)
      ru = -ru
      if cu > cnt[u]: continue
      if cu == cnt[u] and ru < rem[u]: continue
      for i in range(edge_idx[u], edge_idx[u + 1]):
        _, v, d = g[i]
        if d > l: continue
        cv, rv = cu, ru
        if d > rv:
          rv = l
          cv += 1
        rv -= d
        if cv > cnt[v]: continue
        if cv == cnt[v] and rv < rem[v]: continue
        cnt[v], rem[v] = cv, rv
        heapq.heappush(hq, (cv, -rv, v))
    return cnt

  cnt = np.empty((n, n), np.int64)
  for i in range(n):
    cnt[i] = dijkstra(i)

  for i in range(len(st)):
    s, t = st[i]
    print(-1 if cnt[s, t] == inf else cnt[s, t])



def main() -> typing.NoReturn:
  n, m, l = map(int, input().split())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  abc = I[:m * 3].reshape(m, 3)
  abc[:, :2] -= 1
  st = I[m * 3 + 1:].reshape(-1, 2) - 1
  solve(n, l, abc, st)


main()
