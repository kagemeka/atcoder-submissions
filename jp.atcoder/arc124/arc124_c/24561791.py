import typing
import sys
from functools import (
  lru_cache,
)



def gcd(a: int, b: int) -> int:
  if not b: return a
  return gcd(b, a % b)



def lcm(a: int, b: int) -> int:
  return a // gcd(a, b) * b


def solve(
  n: int,
  ab: typing.Iterator[
    typing.Tuple[int, int],
  ],
) -> typing.NoReturn:
  ab = list(ab)


  @lru_cache(maxsize=None)
  def dfs(
    i: int,
    gx: int,
    gy: int,
  ) -> int:
    if i == n:
      return lcm(gx, gy)
    a, b = ab[i]
    lx = dfs(
      i + 1,
      gcd(gx, a),
      gcd(gy, b),
    )
    ly = dfs(
      i + 1,
      gcd(gx, b),
      gcd(gy, a),
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
