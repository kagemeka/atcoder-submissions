import typing
from functools import (
  lru_cache,
)


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:

  s = [0] * (n + 1)
  for i in range(n):
    s[i + 1] = s[i] + a[i]

  @lru_cache(maxsize=None)
  def dfs(
    l: int,
    r: int,
  ) -> typing.NoReturn:
    if r - l == 1: return 0
    return min(
      dfs(l, m) + dfs(m, r)
      for m in range(l + 1, r)
    ) + s[r] - s[l]


  print(dfs(0, n))



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)




main()
