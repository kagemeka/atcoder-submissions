import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(s: np.ndarray, k: int) -> typing.NoReturn:
  n = len(s)
  d = np.sum(s[:-1] != s[1:])
  cnt = n - 1 if k >= (d + 1) // 2 else n - 1 - d + k * 2
  print(cnt)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  s = [0 if x == 'L' else 1 for x in input()]
  s = np.array(s)
  solve(s, k)


main()
