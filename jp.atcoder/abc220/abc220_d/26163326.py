import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  mod = 998244353

  dp = np.zeros(10, np.int64)
  dp[a[0]] = 1
  for i in range(n - 1):
    ndp = np.zeros(10, np.int64)
    for j in range(10):
      ndp[(j + a[i + 1]) % 10] += dp[j]
      ndp[(j * a[i + 1]) % 10] += dp[j]
    dp = ndp % mod
  for x in dp:
    print(x)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
