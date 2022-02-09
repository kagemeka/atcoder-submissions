import typing
import sys
import numpy as np



def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  dp = np.zeros(
    (n + 1, n + 1),
    dtype=np.int64,
  )
  s = np.zeros(n + 1, np.int64)
  s[1:] = a
  s = s.cumsum()
  for w in range(2, n + 1):
    for l in range(n - w + 1):
      r = l + w
      v = 1 << 50
      for m in range(l + 1, r):
        v = min(
          v,
          dp[l, m] + dp[m, r],
        )
      v += s[r] - s[l]
      dp[l, r] = v

  print(dp[0][n])



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
  import numba as nb
  from numba.pycc import CC
  cc = CC('my_module')
  fn = solve
  signature = (nb.i8, nb.i8[:])
  cc.export(
    fn.__name__,
    signature,
  )(fn)

  cc.compile()
  exit(0)


from my_module import solve
main()
