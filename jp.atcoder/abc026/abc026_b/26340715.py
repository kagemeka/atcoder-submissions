import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(r: np.ndarray) -> typing.NoReturn:
  n = len(r)
  s = np.zeros(n + 1)
  s[1:] = r * r * np.pi
  s = np.sort(s)[::-1]
  res = s[::2].sum() - s[1::2].sum()
  print(res)



def main() -> typing.NoReturn:
  n = int(input())
  r = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(r)


main()
