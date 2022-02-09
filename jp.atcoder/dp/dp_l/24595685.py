import typing
import numpy as np
import sys


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  dp = np.zeros(
    (n + 1, n + 1),
    dtype=np.int64,
  )
  for w in range(1, n + 1):
    for l in range(n - w + 1):
      r = l + w
      x = dp[l + 1, r]
      y = dp[l, r - 1]
      if (n - w) & 1 ^ 1:
        dp[l, r] = max(
          x + a[l],
          y + a[r - 1],
        )
        continue
      dp[l, r] = min(
        x - a[l],
        y - a[r - 1],
      )

  print(dp[0, n])



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import i8
  from numba.pycc import CC
  cc = CC('my_module')
  fn = solve
  signature = (i8, i8[:])

  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
