import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, x: int) -> typing.NoReturn:
  n = len(a)


  r = 0
  cnt = 0
  for i in a:
    to_eat = max(0, r + i - x)
    cnt += to_eat
    r = i - to_eat
  print(cnt)


def main() -> typing.NoReturn:
  n, x = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, x)


main()
