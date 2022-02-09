import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def mod_cumprod(a: np.ndarray, mod) -> typing.NoReturn:
  for i in range(len(a) - 1): a[i + 1] = a[i + 1] * a[i] % mod


@nb.njit
def mod_factorial(n: int, mod: int) -> np.ndarray:
  a = np.arange(n)
  a[0] = 1
  mod_cumprod(a, mod)
  return a


@nb.njit
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit
def mod_inverse(n: int, mod: int) -> int:
  return mod_pow(n, mod - 2, mod)


@nb.njit
def mod_factorial_inverse(n: int, mod: int) -> np.ndarray:
  a = np.arange(1, n + 1)
  a[-1] = mod_inverse(mod_factorial(n, mod)[-1], mod)
  mod_cumprod(a[::-1], mod)
  return a


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7

  fact = mod_factorial(1 << 20, mod)
  ifact = mod_factorial_inverse(1 << 20, mod)

  def mod_choose(n, k):
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok


  def count(k):
    cnt = 0
    for x in range(1, n + 1):
      m = n - (k - 1) * (x - 1)
      if m < x: break
      cnt += mod_choose(m, x)
    return cnt

  for k in range(1, n + 1):
    print(count(k))


def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


main()
