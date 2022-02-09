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


@nb.njit((nb.i8, ) * 3, cache=True)
def solve(x: int, y: int, z: int) -> typing.NoReturn:
  mod = 1_000_000_007

  denominator = (x * (y + z) - y * z) % mod
  denominator = mod_pow(denominator % mod, mod - 2, mod)
  r = (y * z - x * z) % mod * denominator % mod
  c = (y * z - x * y) % mod * denominator % mod
  print(r, c)



def main() -> typing.NoReturn:
  a = int(input())
  b = int(input())
  c = int(input())
  solve(a, b, c)

main()
