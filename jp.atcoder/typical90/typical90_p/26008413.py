import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ) * 4, cache=True)
def solve(n: int, a: int, b: int, c: int) -> typing.NoReturn:
  m = 10_000

  mn = m
  for i in range(m):
    for j in range(m - i):
      k, r = divmod(n - i * a - j * b, c)
      if r or k < 0: continue
      mn = min(mn, i + j + k)
  print(mn)


def main() -> typing.NoReturn:
  n = int(input())
  a, b, c = map(int, input().split())
  solve(n, a, b, c)


main()
