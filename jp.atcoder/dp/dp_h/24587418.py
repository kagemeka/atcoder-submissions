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


OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import b1
  from numba.pycc import CC
  cc = CC('my_module')
  fn = solve
  signature = (b1[:, :], )
  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
