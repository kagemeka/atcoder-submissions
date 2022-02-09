import typing
import sys
import numpy as np


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  dp = np.full(
    (n + 1, n + 1, n + 1),
    -1,
    dtype=np.float64,
  )
  dp[0, 0, 0] = 0
  for i in range(n + 1):
    for j in range(n + 1):
      for k in range(n + 1):
        if i + j + k > n:
          continue
        s = i + j + k
        if s == 0: continue
        e = n
        if i > 0:
          e += i * dp[i - 1][j + 1][k]
        if j > 0:
          e += j * dp[i][j - 1][k + 1]
        if k > 0:
          e += k * dp[i][j][k - 1]
        dp[i][j][k] = e / s

  i = (a == 3).sum()
  j = (a == 2).sum()
  k = (a == 1).sum()
  print(dp[i][j][k])



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
  from numba import njit, i8

  fn = solve
  signature = (i8, i8[:])

  from numba.pycc import CC
  cc = CC('my_module')
  cc.export(
    fn.__name__,
    signature,
  )(fn)

  cc.compile()
  exit(0)


from my_module import solve
main()
