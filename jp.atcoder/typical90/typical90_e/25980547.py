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
  pow10_pow2 = np.empty(61, np.int64)
  pow10_pow2[0] = 10 % b
  for i in range(60):
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

  def _pow(x, n):
    y = _identity()
    d = 0
    while n:
      if n & 1: y = _mul(y, x, d)
      x = _mul(x, x, d)
      d += 1
      n >>= 1
    return y

  a = np.zeros(b, np.int64)
  for x in c: a[x % b] += 1
  a = _pow(a, n)
  print(a[0])


def main() -> typing.NoReturn:
  n, b, k = map(int, input().split())
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, b, c)


main()
