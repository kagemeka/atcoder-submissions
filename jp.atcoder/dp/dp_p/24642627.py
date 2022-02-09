import typing
import sys


def solve(
  n: int,
  xy: typing.Iterable[
    typing.Tuple[int, int],
  ],
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  g = [
    [] for _ in range(n)
  ]
  for x, y in xy:
    x -= 1; y -= 1
    g[x].append(y)
    g[y].append(x)


  q = [0]
  parent = [-1] * n
  order = []
  for u in q:
    order.append(u)
    for v in g[u]:
      if v == parent[u]:
        continue
      parent[v] = u
      q.append(v)


  dp = [
    [1] * 2
    for _ in range(n)
  ]


  for u in q[:0:-1]:
    v = parent[u]
    w, b = dp[u]
    dp[v][0] *= w + b
    dp[v][0] %= mod
    dp[v][1] *= w
    dp[v][1] %= mod

  print(sum(dp[0]) % mod)


def main() -> typing.NoReturn:
  n = int(input())
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  xy = zip(*[xy] * 2)
  solve(n, xy)



main()
