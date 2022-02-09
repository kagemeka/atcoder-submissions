import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def ext_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
  if not b:
    return a, 1, 0
  q, r = divmod(a, b)
  g, s, t = ext_gcd(b, r)
  return g, t, s - q * t



@nb.njit((nb.i8, ) * 3, cache=True)
def solve(n: int, s: int, k: int) -> typing.NoReturn:
  g, x, y = ext_gcd(k, n)
  if s % g:
    print(-1)
    return
  s //= g
  k //= g
  n //= g
  c = -s * x % n
  print(c)



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, s, k = map(int, input().split())
    solve(n, s, k)

main()
