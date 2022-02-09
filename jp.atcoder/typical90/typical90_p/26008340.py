import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ) * 4, cache=True)
def solve(n: int, a: int, b: int, c: int) -> typing.NoReturn:
  m = 10_000

  mn = m
  for i in range(m):
    s0 = n - i * a
    if s0 < 0: break
    for j in range(m):
      s = s0 - j * b
      if s < 0: break
      k, r = divmod(s, c)
      if r: continue
      mn = min(mn, i + j + k)
  print(mn)


def main() -> typing.NoReturn:
  n = int(input())
  a, b, c = map(int, input().split())
  solve(n, a, b, c)


main()
