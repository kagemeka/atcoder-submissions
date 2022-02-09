import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def mod_cumprod(a: np.ndarray, mod: int) -> typing.NoReturn:
  for i in range(len(a) - 1): a[i + 1] = a[i + 1] * a[i] % mod


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
def mod_factorial(n: int, mod: int) -> np.ndarray:
  a = np.arange(n)
  a[0] = 1
  mod_cumprod(a, mod)
  return a


@nb.njit
def mod_factorial_inverse(n: int, p: int) -> np.ndarray:
  a = np.arange(1, n + 1)
  a[-1] = mod_inverse(mod_factorial(n, p)[-1], p)
  mod_cumprod(a[::-1], p)
  return a



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  p = len(a)
  fact = mod_factorial(p, p)
  ifact = mod_factorial_inverse(p, p)
  def mod_choose(n, k):
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % p * ifact[k] % p * ok

  b = np.zeros(p, np.int64)

  def add_polynomial(i):
    nonlocal b
    pow_neg_i = np.empty(p, np.int64)
    pow_neg_i[0] = 1
    for j in range(p - 1):
      pow_neg_i[j + 1] = pow_neg_i[j] * (-i) % p
    for j in range(p):
      b[p - 1 - j] -= pow_neg_i[j] * mod_choose(p - 1, j) % p
    b[0] += 1
    b %= p

  for i in range(p):
    if a[i] == 0: continue
    add_polynomial(i)

  for i in b:
    print(i)


def main() -> typing.NoReturn:
  p = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a)


main()
