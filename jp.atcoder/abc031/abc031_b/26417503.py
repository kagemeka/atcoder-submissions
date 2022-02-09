import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8, nb.i8[:]), cache=True)
def solve(l: int, h: int, a: np.ndarray) -> typing.NoReturn:
  for x in a:
    if x < l:
      print(l - x)
    elif l <= x <= h:
      print(0)
    else:
      print(-1)


def main() -> typing.NoReturn:
  l, h = map(int, input().split())
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(l, h, a)


main()
