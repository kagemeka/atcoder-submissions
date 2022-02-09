import typing
import sys
import numpy as np
import scipy.special


def solve(n: int, d: int, x: int, y: int) -> typing.NoReturn:
  if x % d or y % d:
    print(0)
    return
  x, y = abs(x) // d, abs(y) // d
  if n < x + y or (n - x - y) & 1:
    print(0)
    return

  k = n - x - y
  alpha = pow(.5, n)
  tot = 0
  for i in range(0, k + 1, 2):
    d = i // 2
    u = y + d
    l = (k - i) // 2
    r = x + l
    tmp = alpha * scipy.special.comb(n, d, exact=True)
    tmp *= scipy.special.comb(n - d, u, exact=True)
    tmp *= scipy.special.comb(n - d - u, l, exact=True)
    tmp *= scipy.special.comb(n - d - u - l, r, exact=True)
    tot += tmp * alpha

  print(tot)


def main() -> typing.NoReturn:
  n, d = map(int, input().split())
  x, y = map(int, input().split())
  solve(n, d, x, y)

main()
