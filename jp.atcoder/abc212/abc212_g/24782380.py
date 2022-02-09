import typing
import numpy as np
import numba as nb



@nb.njit
def find_divisors(
  n: int,
) -> np.array:
  i = np.arange(int(n ** .5))
  i += 1
  i = i[n % i == 0]
  i = np.hstack((i, n // i))
  return np.unique(i)



@nb.njit
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



@nb.njit(
  (nb.i8, ),
  cache=True,
)
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


main()
