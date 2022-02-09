import typing
import numpy as np



def solve(r: int, g: int, b: int) -> typing.NoReturn:
  inf = 1 << 30
  m = k = 1000
  x = np.empty(k, np.int64)
  x[:r + 1] = -100
  x[r + 1:r + g + 1] = 0
  x[r + g + 1:] = 100
  dp = np.full(k, inf, np.int64)
  dp[0] = 0

  for i in range(-m, m):
    np.minimum(
      dp[1:],
      dp[:-1] + np.abs(i - x[1:]),
      out=dp[1:],
    )
  print(dp[r + g + b])


def main() -> typing.NoReturn:
  r, g, b = map(int, input().split())
  solve(r, g, b)


main()
