import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8, nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  k: int,
  g: np.array,
) -> typing.NoReturn:
  mod = 998244353

  m = g.shape[0]
  dp = np.zeros(n, np.int64)
  dp[0] = 1

  for _ in range(k):
    s = 0
    for x in dp:
      s += x
      s %= mod
    ndp = np.full(
      n,
      s,
      np.int64,
    )
    for u in range(n):
      ndp[u] -= dp[u]
      ndp[u] %= mod
    for i in range(m):
      u, v = g[i]
      ndp[u] -= dp[v]
      ndp[u] %= mod
      ndp[v] -= dp[u]
      ndp[v] %= mod
    dp = ndp

  print(dp[0])


def main() -> typing.NoReturn:
  n, m, k = map(
    int, input().split(),
  )
  g = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, k, g)


main()
