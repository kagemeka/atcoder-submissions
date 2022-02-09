import typing
import sys
import numpy as np
import numba as nb


mod = 10 ** 9 + 7

@nb.njit((nb.i8, nb.i8, nb.i8[:]), cache=True)
def solve(
  n: int,
  b: int,
  c: np.ndarray,
) -> typing.NoReturn:
  m = 60
  pow10_pow2 = np.empty(m, np.int64)
  pow10_pow2[0] = 10 % b
  for i in range(m - 1):
    pow10_pow2[i + 1] = pow10_pow2[i] ** 2 % b

  def _mul(x, y, d):
    z = np.zeros(b, np.int64)
    for r in range(b):
      for i in range(b):
        j = (r - pow10_pow2[d] * i) % b
        z[r] += x[i] * y[j] % mod
        z [r] %= mod
    return z % mod

  def _identity():
    e = np.zeros(b, np.int64)
    e[0] = 1
    return e

  a = np.zeros((m, b), np.int64)
  for x in c: a[0, x % b] += 1
  for i in range(m - 1):
    a[i + 1] = _mul(a[i], a[i], i)

  def _pow(n):
    y = _identity()
    d = 0
    while n:
      if n & 1: y = _mul(y, a[d], d)
      d += 1
      n >>= 1
    return y

  print(_pow(n)[0])


def main() -> typing.NoReturn:
  n, b, k = map(int, input().split())
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, b, c)


main()
