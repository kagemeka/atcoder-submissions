import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ), cache=True)
def euler_totient(n: int) -> int:
  c, i = n, 1
  while i * i <= n:
    i += 1
    if n % i: continue
    c = c // i * (i - 1)
    while n % i == 0: n //= i
  if n > 1: c = c // n * (n - 1)
  return c


@nb.njit((nb.i8, nb.i8), cache=True)
def gcd(a: int, b: int) -> int:
  while b: a, b = b, a % b
  return a


@nb.njit((nb.i8, nb.i8, nb.i8), cache=True)
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit((nb.i8, ) * 3, cache=True)
def solve(n: int, s: int, k: int) -> typing.NoReturn:
  g = gcd(k, n)
  if s % g:
    print(-1)
    return
  s //= g
  k //= g
  n //= g
  phi = euler_totient(n)
  k_inv = mod_pow(k, phi - 1, n)
  print(-s * k_inv % n)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, s, k = map(int, input().split())
    solve(n, s, k)

main()
