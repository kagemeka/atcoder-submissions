import typing
import sys
from math import (
  gcd,
  lcm,
)
from functools import (
  lru_cache,
)


def solve(
  n: int,
  ab: typing.Iterator[
    typing.Tuple[int, int],
  ],
) -> typing.NoReturn:


  a, b = [], []
  for x, y in ab:
    a.append(x)
    b.append(y)


  @lru_cache(maxsize=None)
  def dfs(
    i: int,
    gx: int,
    gy: int,
  ) -> int:
    if i == n:
      return lcm(gx, gy)

    lx = dfs(
      i + 1,
      gcd(gx, a[i]),
      gcd(gy, b[i]),
    )
    ly = dfs(
      i + 1,
      gcd(gx, b[i]),
      gcd(gy, a[i]),
    )
    return max(lx, ly)

  print(dfs(0, 0, 0))


def main() -> typing.NoReturn:
  n = int(input())
  ab = map(
    int,
    sys.stdin.read().split(),
  )
  ab = zip(*[ab] * 2)
  solve(n, ab)


main()
