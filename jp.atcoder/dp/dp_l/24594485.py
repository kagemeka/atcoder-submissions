import typing
import sys
sys.setrecursionlimit(1 << 25)
from functools import (
  lru_cache,
)


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  @lru_cache(maxsize=None)
  def dfs(
    l: int,
    r: int,
  ) -> int:
    if l + r == n: return 0
    x = dfs(l + 1, r)
    y = dfs(l, r + 1)
    r = -1 - r
    if (l + r) & 1 ^ 1:
      return max(
        x + a[l],
        y + a[r],
      )
    return min(
      x - a[l],
      y - a[r],
    )

  print(-dfs(0, 0))




def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)


main()
