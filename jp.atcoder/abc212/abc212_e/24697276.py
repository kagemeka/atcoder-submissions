import typing
import sys




def solve(
  n: int,
  m: int,
  k: int,
  uv: typing.Iterator[
    typing.Tuple[int, int],
  ],
) -> typing.NoReturn:
  mod = 998244353
  g = [
    [i] for i in range(n)
  ]
  for u, v in uv:
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


  dp = [0] * n
  dp[0] = 1

  for _ in range(k):
    s = sum(dp) % mod
    ndp = [s] * n
    for u in range(n):
      for v in g[u]:
        ndp[u] -= dp[v]
      ndp[u] %= mod
    dp = ndp

  print(dp[0])
  ...


def main() -> typing.NoReturn:
  n, m, k = map(
    int, input().split(),
  )
  uv = map(
    int,
    sys.stdin.read().split(),
  )
  uv = zip(*[uv] * 2)
  solve(n, m, k, uv)



main()
