import typing
import sys
import numpy as np



def main() -> typing.NoReturn:
  n, w = map(
    int, input().split(),
  )
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  dp = np.zeros(
    w + 1,
    dtype=np.int64,
  )
  for a, b in ab:
    np.maximum(
      dp[a:],
      dp[:-a] + b,
      out=dp[a:],
    )
  print(dp[-1])


main()
