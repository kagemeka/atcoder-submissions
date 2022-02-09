import typing
import numpy as np



def main() -> typing.NoReturn:
  n = int(input())
  p = np.array(
    input().split(),
    dtype=np.float128,
  )
  dp = np.zeros(
    n + 1,
    np.float128,
  )
  dp[0] = 1
  for x in p:
    dp[1:] = (
      dp[:-1] * x
      + dp[1:] * (1 - x)
    )
  print(dp[(n + 1) // 2])


main()
