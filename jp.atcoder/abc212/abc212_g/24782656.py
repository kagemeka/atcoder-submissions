import typing
import numpy as np


def find_divisors(
  n: int,
) -> np.array:
  i = np.arange(int(n ** .5))
  i += 1
  i = i[n % i == 0]
  i = np.hstack((i, n // i))
  return np.unique(i)


def euler_totient(
  n: int,
) -> int:
  c = n
  p = 2
  while p * p <= n:
    if n % p:
      p += 1
      continue
    c = c // p * (p - 1)
    while not n % p: n //= p
  if n > 1:
    c = c // n * (n - 1)
  return c


def solve(
  p: int,
) -> typing.NoReturn:
  n = p - 1
  divs = find_divisors(n)
  mod = 998244353
  s = 1
  for d in divs:
    s += euler_totient(
      d,
    ) % mod * (d % mod) % mod
    s %= mod
  print(s)


def main() -> typing.NoReturn:
  p = int(input())
  solve(p)


import sys
OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import njit, i8
  from numba.pycc import CC
  cc = CC('my_module')
  fn = solve
  signature = (i8, )

  find_divisors = njit(
    find_divisors,
  )
  euler_totient = njit(
    euler_totient,
  )

  cc.export(
    fn.__name__,
    signature,
  )(fn)

  cc.compile()
  exit(0)


from my_module import solve
main()
