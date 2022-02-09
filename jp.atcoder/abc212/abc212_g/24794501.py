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



def gpf(
  n: int = 1 << 20,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n - 1:
    i += 1
    if s[i] == i: s[i::i] = i
  return s


def lpf(
  n: int = 1 << 20,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n - 1:
    i += 1
    if s[i] != i: continue
    j = np.arange(i, n, i)
    s[j][s[j] == j] = i
  return s


def sieve_of_eratosthenes(
  n: int = 1 << 20,
) -> np.array:
  return gpf(n) == np.arange(n)



def prime_numbers(
  n: int = 1 << 20,
) -> np.array:
  s = sieve_of_eratosthenes(n)
  return np.flatnonzero(s)



def euler_totient(
  n: int,
  prime_numbers: np.array,
) -> int:
  c = n
  for p in prime_numbers:
    if p * p > n: break
    if n % p: continue
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
  pn = prime_numbers(1 << 20)
  mod = 998244353
  c = 1
  for d in divs:
    e = euler_totient(d, pn)
    e %= mod
    d %= mod
    c += e * d % mod
    c %= mod
  print(c)


def main() -> typing.NoReturn:
  p = int(input())
  solve(p)




import sys
OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import njit, i8
  find_divisors = njit(
    find_divisors,
  )
  lpf = njit(lpf)
  gpf = njit(gpf)
  sieve_of_eratosthenes = njit(
    sieve_of_eratosthenes,
  )
  prime_numbers = njit(
    prime_numbers,
  )
  euler_totient = njit(
    euler_totient,
  )
  fn = solve
  signature = (i8, )
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
