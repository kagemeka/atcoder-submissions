import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def mod_cumprod(
  a: np.array,
  mod: int,
) -> np.array:
  n = a.shape[0]
  for i in range(n - 1):
    a[i + 1] *= a[i]
    a[i + 1] %= mod


@nb.njit
def mod_pow(
  x: int,
  n: int,
  mod: int,
) -> int:
  if n == 0: return 1
  y = mod_pow(x, n >> 1, mod)
  y = y * y % mod
  if n & 1: y = y * x % mod
  return y



@nb.njit
def mod_factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(n)
  a[0] = 1
  mod_cumprod(a, mod)
  return a


@nb.njit
def inv_mod_factorial(
  n: int,
  mod: int,
) -> np.array:
  x = mod_factorial(n, mod)[-1]
  a = np.arange(1, n + 1)
  a[-1] = mod_pow(x, mod - 2, mod)
  mod_cumprod(a[::-1], mod)
  return a



@nb.njit
def mod_choose(
  n: int,
  r: int,
  mod: int,
  fact: np.array,
  ifact: np.array,
) -> int:
  ok = (0 <= r) & (r <= n)
  c = fact[n] * ifact[n - r] % mod * ifact[r] % mod
  return c * ok


@nb.njit
def inv_mod_choose(
  n: int,
  r: int,
  mod: int,
  fact: np.array,
  ifact: np.array,
) -> int:
  ok = (0 <= r) & (r <= n)
  c = ifact[n] * fact[n - r] % mod * fact[r] % mod
  return c * ok



@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def solve(
  c: np.array,
) -> typing.NoReturn:
  n = c.size
  a = np.unique(c)
  m = a.size
  c = np.searchsorted(a, c)
  c = np.bincount(np.bincount(c))
  idx = np.flatnonzero(c)

  mod = 998244353
  fact = mod_factorial(1 << 20, mod)
  ifact = inv_mod_factorial(1 << 20, mod)

  def mod_choose(n, k):
    ok = (0 <= k) & (k <= n)
    c = fact[n] * ifact[n - k] % mod * ifact[k] % mod
    return c * ok

  def inv_mod_choose(n, k):
    ok = (0 <= k) & (k <= n)
    c = ifact[n] * fact[n - k] % mod * fact[k] % mod
    return c * ok

  def count_up(k):
    s = 0
    for i in idx:
      s -= mod_choose(n - i, k) * c[i] % mod
    s %= mod
    s *= inv_mod_choose(n, k)
    return (s + m) % mod

  for k in range(1, n + 1):
    print(count_up(k))


def main() -> typing.NoReturn:
  n = int(input())
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(c)


main()
