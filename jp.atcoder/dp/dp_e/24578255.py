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

  inf = 1 << 40
  dp = np.full(
    1 << 17,
    inf,
    dtype=np.int64,
  )
  dp[0] = 0
  for a, b in ab:
    np.minimum(
      dp[b:],
      dp[:-b] + a,
      out=dp[b:],
    )
  np.minimum.accumulate(
    dp[::-1],
    out=dp[::-1],
  )
  v = np.searchsorted(
    dp,
    w,
    side='right',
  ) - 1
  print(v)



main()
