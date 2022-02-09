import typing
from collections import (
  Counter,
)
from functools import (
  lru_cache,
)
import sys
sys.setrecursionlimit(1 << 25)



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  @lru_cache(maxsize=None)
  def dfs(
    i: int,
    j: int,
    k: int,
  ) -> typing.NoReturn:
    nonlocal n
    s = i + j + k
    if s == 0: return 0
    e = n / s
    if i > 0:
      e += i / s * dfs(
        i - 1,
        j + 1,
        k,
      )
    if j > 0:
      e += j / s * dfs(
        i,
        j - 1,
        k + 1,
      )
    if k > 0:
      e += k / s * dfs(
        i,
        j,
        k - 1,
      )
    return e

  c = Counter(a)
  print(dfs(c[3], c[2], c[1]))


def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)


main()
