import typing
import sys
import numpy as np


def solve(
  g: np.array,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  h, w = g.shape
  dp = np.zeros(
    w,
    np.int64,
  )
  dp[0] = 1
  for i in range(h):
    for j in range(w - 1):
      dp[j + 1] += (
        dp[j] * g[i, j]
      )
    dp *= g[i]
    dp %= mod
  print(dp[-1])


def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  g = [
    [
      x == '.'
      for x in list(input())
    ]
    for _ in range(h)
  ]
  g = np.array(g)
  solve(g)


main()
