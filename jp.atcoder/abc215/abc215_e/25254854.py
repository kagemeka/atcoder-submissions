import typing
import sys
import numpy as np



def solve(
  a: np.array,
) -> typing.NoReturn:
  n = a.size
  m = 10
  mod = 998244353
  dp = np.zeros((1 << m, m), dtype=np.int64)

  for i in range(n):
    x = a[i]
    for s in range((1 << m) - 1, -1, -1):
      if ~s >> x & 1: continue
      dp[s, x] *= 2
      u = s & ~(1 << x)
      for j in range(m):
        if ~u >> j & 1: continue
        dp[s, x] += dp[u, j]
      dp[s, x] %= mod
    dp[1 << x, x] += 1
  print(dp.sum() % mod)


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  a = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('A')
  solve(a)



OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  import numba as nb
  fn = solve
  sig = (nb.i8[:], )
  from numba.pycc import CC
  cc = CC('my_module')
  cc.export(
    fn.__name__,
    sig,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
