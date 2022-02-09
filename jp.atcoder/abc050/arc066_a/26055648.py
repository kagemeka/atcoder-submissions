import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  # b = np.bincount(a, minlength=n)
  b = np.zeros(n, np.int64)
  for x in a: b[x] += 1
  if n & 1:
    b[0] += 1
    b = b[::2]
  else:
    b = b[1::2]
  mod = 10 ** 9 + 7
  ans = mod_pow(2, n // 2, mod) if np.all(b == 2) else 0
  print(ans)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
