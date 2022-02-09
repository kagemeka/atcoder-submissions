import typing
import sys
sys.setrecursionlimit(1 << 20)
from functools import (
  lru_cache,
)



def solve(
  k: int,
  a: int,
) -> typing.NoReturn:
  @lru_cache(maxsize=None)
  def dfs(
    x: int,
  ) -> bool:
    win = 0
    for d in a:
      if x - d < 0: continue
      win |= ~dfs(x - d)
    return win

  win = dfs(k)
  print(
    'First' if win
    else 'Second',
  )



def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  *a, = map(
    int, input().split(),
  )
  solve(k, a)


main()
