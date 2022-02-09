import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8[:]), cache=True)
def solve(m: int, f: np.ndarray) -> typing.NoReturn:
  n = len(f)

  last = np.full(m, -1, np.int64)
  prev = np.empty(n, np.int64)
  for i in range(n):
    prev[i] = last[f[i]]
    last[f[i]] = i

  mod = 1_000_000_007

  dp = np.zeros(n + 1, np.int64)
  dp[0] = 1
  l = 0
  ptn = 0
  for i in range(n):
    ptn += dp[i]
    while l < prev[i] + 1:
      ptn -= dp[l]
      l += 1
    ptn %= mod
    dp[i + 1] = ptn
  print(dp[-1])


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  f = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ) - 1
  solve(m, f)


main()
