import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def bit_count(n: int) -> int:
  cnt = 0
  while n:
    cnt += n & 1
    n >>= 1
  return cnt


@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, xy: np.ndarray) -> typing.NoReturn:
  n = len(a)
  m = len(xy)

  inf = 1 << 60
  cost = np.zeros((n, n), np.int64)
  for i in range(m):
    x, y = xy[i]
    cost[x, y] = cost[y, x] = inf


  dp = np.full((1 << n, n), inf, np.int64)
  for i in range(n):
    dp[1 << i, i] = a[i, 0]

  for s in range(1 << n):
    i = bit_count(s) - 1
    for v in range(n):
      if ~s >> v & 1: continue
      t = s & ~(1 << v)
      for u in range(n):
        if ~t >> u & 1: continue
        dp[s, v] = min(
          dp[s, v],
          dp[t, u] + cost[u, v] + a[v, i]
        )
  mn = dp[-1].min()
  print(-1 if mn == inf else mn)



def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  a = I[:n * n].reshape(n, n)
  xy = I[n * n + 1:].reshape(-1, 2) - 1
  solve(a, xy)


main()
