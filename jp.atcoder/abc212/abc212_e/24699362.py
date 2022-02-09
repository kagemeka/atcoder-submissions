import typing
import sys


def solve(
  n: int,
  k: int,
  uv: typing.List[
    typing.Tuple[int, int],
  ],
) -> typing.NoReturn:
  mod = 998244353
  dp = [0] * n
  dp[0] = 1

  for _ in range(k):
    s = sum(dp) % mod
    ndp = [s] * n
    for u in range(n):
      ndp[u] -= dp[u]
      ndp[u] %= mod
    for u, v in uv:
      ndp[u] -= dp[v]
      ndp[v] -= dp[u]
      ndp[u] %= mod
      ndp[v] %= mod
    dp = ndp
  print(dp[0])


def main() -> typing.NoReturn:
  n, m, k = map(
    int, input().split(),
  )
  uv = map(
    lambda x: int(x) - 1,
    sys.stdin.read().split(),
  )
  *uv, = zip(*[uv] * 2)
  solve(n, k, uv)



main()
