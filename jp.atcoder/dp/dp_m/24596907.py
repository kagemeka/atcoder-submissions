import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  k: int,
  a: np.array,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  dp = np.zeros(
    k + 1,
    dtype=np.int64,
  )
  dp[0] = 1
  for x in a:
    x += 1
    dp[x:] -= dp.copy()[:-x]
    dp = np.cumsum(dp)
    dp %= mod
  print(dp[-1])


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(k, a)


main()
