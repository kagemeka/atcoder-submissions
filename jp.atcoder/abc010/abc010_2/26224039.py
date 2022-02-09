import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def count_petals(n: int) -> int:
  cnt = 0
  while n % 2 == 0 or n % 3 == 2:
    cnt += 1
    n -= 1
  return cnt


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  cnt = 0
  for x in a:
    cnt += count_petals(x)
  print(cnt)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
