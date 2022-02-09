import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def mod_cumprod(a: np.ndarray, mod: int) -> typing.NoReturn:
  for i in range(a.size - 1): a[i + 1] = a[i + 1] * a[i] % mod


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = a.size
  a = np.hstack((np.array([0]), a))
  a = np.unique(a)
  d = a[1:] - a[:-1] + 1
  mod = 10 ** 9 + 7
  mod_cumprod(d, mod)
  print(d[-1])

def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
