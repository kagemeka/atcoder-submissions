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


  parent = [-1] * n
  def dfs(
    u: int,
  ) -> typing.Tuple[int, int]:
    black = white = 1
    for v in g[u]:
      if v == parent[u]:
        continue
      parent[v] = u
      b, w = dfs(v)
      black *= w
      black %= mod
      white *= b + w
      white %= mod
    return black, white

  print(sum(dfs(0)) % mod)


def main() -> typing.NoReturn:
  n = int(input())
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  xy = zip(*[xy] * 2)
  solve(n, xy)



main()
