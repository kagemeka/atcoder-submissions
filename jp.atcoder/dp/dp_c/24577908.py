import typing
import numpy as np
import sys


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 3)
  j = np.arange(3)
  j = np.vstack((j + 1, j + 2))
  j %= 3
  dp = np.zeros(
    3,
    dtype=np.int64,
  )
  for x in a:
    dp = dp[j].max(axis=0) + x
  print(dp.max())


main()
