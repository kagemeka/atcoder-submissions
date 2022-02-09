import typing
import sys
sys.setrecursionlimit(1 << 20)
import functools


def solve(
  h: int,
  w: int,
  xy: typing.List[typing.Tuple[int, int]],
) -> typing.NoReturn:

  @functools.lru_cache(maxsize=None)
  def max_count(l: int, r: int, d: int, u: int) -> int:
    def on_grid(x: int, y: int) -> bool:
      return l <= x < r and d <= y < u

    mx = 0
    for x, y in xy:
      if not on_grid(x, y): continue
      s = r - l + u - d - 1
      s += max_count(l, x, d, y)
      s += max_count(l, x, y + 1, u)
      s += max_count(x + 1, r, d, y)
      s += max_count(x + 1, r, y + 1, u)
      mx = max(mx, s)
    return mx

  print(max_count(0, w, 0, h))



def main() -> typing.NoReturn:
  w, h = map(int, input().split())
  n = int(input())
  xy = map(lambda x: int(x) - 1, sys.stdin.read().split())
  xy = list(zip(*[xy] * 2))
  solve(h, w, xy)


main()
