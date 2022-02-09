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
def mod_inverse(n: int, mod: int) -> int:
  return mod_pow(n, mod - 2, mod)


@nb.njit
def mod_factorial_inverse(n: int, mod: int) -> np.ndarray:
  a = np.arange(1, n + 1)
  a[-1] = mod_inverse(mod_factorial(n, mod)[-1], mod)
  mod_cumprod(a[::-1], mod)
  return a


@nb.njit((nb.i8, ) * 4, cache=True)
def solve(h: int, w: int, a: int, b: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  m = 1 << 20
  fact = mod_factorial(m, mod)
  ifact = mod_factorial_inverse(m, mod)

  def choose(n, k):
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok


  cnt = 0
  i = h - a - 1
  for j in range(b, w):
    c = choose(i + j, j) * choose(h + w - i - j - 3, w - 1 - j)
    cnt += c % mod
  print(cnt % mod)




def main() -> typing.NoReturn:
  h, w, a, b = map(int, input().split())
  solve(h, w, a, b)


main()
