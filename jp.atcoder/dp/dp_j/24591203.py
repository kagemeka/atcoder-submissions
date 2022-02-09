import typing
from collections import (
  Counter,
)
import sys
sys.setrecursionlimit(1 << 25)



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  cache = [
    [
      [-1] * (n + 1)
      for _ in range(n + 1)
    ]
    for _ in range(n + 1)
  ]
  cache[0][0][0] = 0

  def dfs(
    i: int,
    j: int,
    k: int,
  ) -> typing.NoReturn:
    if (
      i < 0 or j < 0 or k < 0
    ): return 0
    e = cache[i][j][k]
    if e != -1: return e
    s = i + j + k
    if s == 0: return 0
    e = n
    e += i * dfs(
      i - 1,
      j + 1,
      k,
    )
    e += j * dfs(
      i,
      j - 1,
      k + 1,
    )
    e += k * dfs(
      i,
      j,
      k - 1,
    )
    e /= s
    cache[i][j][k] = e
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
