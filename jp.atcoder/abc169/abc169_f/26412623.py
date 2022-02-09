import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, s: int) -> typing.NoReturn:
  n = len(a)

  mod = 998_244_353

  dp = np.zeros(s + 1, np.int64)
  dp[0] = 1
  for x in a:
    for i in range(s, -1, - 1):
      dp[i] *= 2
      if i >= x: dp[i] += dp[i - x]
    dp %= mod
  print(dp[-1])


def main() -> typing.NoReturn:
  n, s = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, s)


main()
