import numpy as np
import typing
import numba as nb


@nb.njit
def cumprod(
  a: np.array,
  mod: int,
) -> typing.NoReturn:
  n = a.size
  for i in range(n - 1):
    a[i + 1] *= a[i]
    a[i + 1] %= mod


@nb.njit
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


@nb.njit
def factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(n); a[0] = 1
  cumprod(a, mod)
  return a


@nb.njit
def inv_factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(1, n + 1)
  x = factorial(n, mod)[-1]
  a[-1] = mpow(x, mod - 2, mod)
  cumprod(a[::-1], mod)
  return a


@nb.njit
def solve(
  n: int,
  m: int,
) -> typing.NoReturn:
  mod = 998244353
  N = 1 << 18
  fact = factorial(N, mod)
  ifact = inv_factorial(N, mod)

  def choose(n, r):
    nonlocal mod, fact, ifact
    ok = (0 <= r) & (r <= n)
    c = fact[n] * ok
    c = c * ifact[n - r] % mod
    return c * ifact[r] % mod

  N = 20
  dp = np.zeros(
    (m + 1, N),
    dtype=np.int64,
  )
  dp[2:, 1] = 1
  for j in range(1, N - 1):
    for i in range(2, m):
      k = np.arange(
        i * 2,
        m + 1,
        i,
      )
      dp[k, j + 1] += dp[i, j]
      dp[k, j + 1] %= mod
  s = dp[2:].sum(axis=0) % mod
  s *= choose(n, np.arange(N))
  s %= mod
  print((s.sum() + 1) % mod)



def main() -> typing.NoReturn:
  n, m = map(
    int,
    input().split(),
  )
  solve(n, m)



import sys


# def aot_compile(
# ) -> typing.NoReturn:
#   from numba import njit, i8
#   global \
#     cumprod, mpow, factorial, \
#     inv_factorial
#   cumprod = njit(cumprod)
#   mpow = njit(mpow)
#   factorial = njit(factorial)
#   inv_factorial = njit(
#     inv_factorial,
#   )
#   fn = solve
#   signature = (i8, i8)
#   from numba.pycc import CC
#   cc = CC('my_module')
#   cc.export(
#     fn.__name__,
#     signature,
#   )(fn)
#   cc.compile()


# if (
#   sys.argv[-1]
#   == 'ONLINE_JUDGE'
# ):
#   aot_compile()
#   exit(0)


# from my_module import solve
main()
