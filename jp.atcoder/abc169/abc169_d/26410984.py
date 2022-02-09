import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:
  def find_k(cnt): # \sum_{j = 1}^{k} 1 \le cnt
    lo, hi = 1, 10
    while hi - lo > 1:
      k = (lo + hi) >> 1
      if k * (k + 1) <= cnt * 2:
        lo = k
      else:
        hi = k
    return lo

  s = 0
  p = 1
  while p * p <= n:
    p += 1
    if n % p: continue
    cnt = 0
    while n % p == 0:
      cnt += 1
      n //= p
    s += find_k(cnt)
  if n > 1: s += 1
  print(s)

def main() -> typing.NoReturn:
  n = int(input())
  solve(n)

main()
