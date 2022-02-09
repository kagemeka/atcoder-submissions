import typing
import numpy as np
# import numba as nb


# @nb.njit
def cumprod(
  a: np.array,
  mod: int,
) -> typing.NoReturn:
  n = a.size
  for i in range(n - 1):
    a[i + 1] *= a[i]
    a[i + 1] %= mod


# @nb.njit
def factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(n); a[0] = 1
  cumprod(a, mod)
  return a


# @nb.njit
def mpow(
  x: int,
  n: int,
  mod: int,
) -> int:
  if n == 0: return 1
  y = mpow(x, n >> 1, mod)
  y = y * y % mod
  if n & 1: y = y * x % mod
  return y


# @nb.njit
def inv_factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(1, n + 1)
  x = factorial(n, mod)[-1]
  a[-1] = mpow(x, mod - 2, mod)
  cumprod(a[::-1], mod)
  return a


# @nb.njit
def lpf(
  n: int = 1 << 20,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n:
    i += 1
    if s[i] != i: continue
    s[i * 2::i] = i
  return s


# @nb.njit
def solve(
  n: int,
  m: int,
) -> typing.NoReturn:
  mod = 998244353
  N = 1 << 20
  fact = factorial(N, mod)
  ifact = inv_factorial(N, mod)

  def choose(n, r):
    ok = (0 <= r) & (r <= n)
    c = fact[n] * ok
    c = c * ifact[r] % mod
    return c * ifact[n - r] % mod

  a = lpf(1 << 18)
  res = 1
  for i in range(2, m + 1):
    tot = 1
    prime = -1
    cnt = 0
    while i >= 1:
      p = a[i]
      i //= p
      if p == prime:
        cnt += 1
        continue
      tot *= choose(
        n + cnt - 1,
        cnt,
      )
      tot %= mod
      prime, cnt = p, 1
    res += tot
    res %= mod
  print(res)


def main():
  n, m = map(
    int,
    input().split(),
  )
  solve(n, m)



import sys


if (
  sys.argv[-1]
  == 'ONLINE_JUDGE'
):
  ''''''
  from numba import njit, i8
  cumprod = njit(cumprod)
  mpow = njit(mpow)
  factorial = njit(factorial)
  inv_factorial = njit(
    inv_factorial,
  )
  lpf = njit(lpf)
  fn = solve
  signature = (i8, i8)
  ''''''
  from numba.pycc import CC
  cc = CC('my_module')
  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
