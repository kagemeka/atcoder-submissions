import typing
import sys
from functools import (
  lru_cache,
)
sys.setrecursionlimit(1 << 20)



def solve(
  n: int,
  xy: typing.Generator,
) -> typing.NoReturn:
  edges = [
    [] for _ in range(n)
  ]
  for x, y in xy:
    edges[x - 1].append(y - 1)

  dist = [0] * n

  @lru_cache(maxsize=None)
  def dfs(
    u: int,
  ) -> int:
    mx = 0
    for v in edges[u]:
      mx = max(mx, dfs(v) + 1)
    dist[u] = mx
    return mx

  for i in range(n):
    dist[i] = dfs(i)

  print(max(dist))



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  xy = zip(*[xy] * 2)
  solve(n, xy)


main()
