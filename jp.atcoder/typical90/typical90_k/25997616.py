import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(dcs: np.ndarray) -> typing.NoReturn:
  n = len(dcs)
  dp = np.zeros(1 << 16, np.int64)
  dcs = dcs[np.argsort(dcs[:, 0], kind='mergesort')]
  for i in range(n):
    d, c, s = dcs[i]
    for k in range(d, c - 1, - 1):
      dp[k] = max(dp[k], dp[k - c] + s)
  print(dp.max())

def main() -> typing.NoReturn:
  n = int(input())
  dcs = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 3)
  solve(dcs)


main()
