import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def mod_cumprod(a: np.ndarray, mod: int) -> typing.NoReturn:
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
def mod_inverse(n: int, p: int) -> int:
  return mod_pow(n, p - 2, p)


@nb.njit
def mod_factorial_inverse(n: int, mod: int) -> np.ndarray:
  a = np.arange(1, n + 1)
  a[-1] = mod_inverse(mod_factorial(n, mod)[-1], mod)
  mod_cumprod(a[::-1], mod)
  return a


@nb.njit
def solve(n: int, k: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  fact = mod_factorial(1 << 18, mod)
  ifact = mod_factorial_inverse(1 << 18, mod)

  def mod_choose(n, k):
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok

  def mod_nHk(n, k):
    return mod_choose(n + k - 1, k)

  print(mod_nHk(n, k))


def main() -> typing.NoReturn:
  n = int(input())
  k = int(input())
  solve(n, k)

main()
