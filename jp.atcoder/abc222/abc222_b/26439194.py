import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, p: int) -> typing.NoReturn:
  cnt = 0
  for x in a:
    cnt += x < p
  print(cnt)


def main() -> typing.NoReturn:
  n, p = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, p)


main()
