import typing
import sys
sys.setrecursionlimit(1 << 25)


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  cache = [
    [None] * (n + 1)
    for _ in range(n + 1)
  ]
  def dfs(
    l: int,
    r: int,
  ) -> int:
    if l + r == n: return 0
    v = cache[l][r]
    if v is not None: return v
    x = dfs(l + 1, r)
    y = dfs(l, r + 1)
    if (l + r) & 1 ^ 1:
      v = max(
        x + a[l],
        y + a[-1 - r],
      )
    else:
      v = min(
        x - a[l],
        y - a[-1 - r],
      )
    cache[l][r] = v
    return v

  print(dfs(0, 0))



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)


main()
