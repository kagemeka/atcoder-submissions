import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def prime_numbers(n: int=1 << 20) -> np.array:
  return np.flatnonzero(sieve_of_eratosthenes(n))


@nb.njit
def sieve_of_eratosthenes(n: int=1 << 20) -> np.array:
  return gpf(n) == np.arange(n)


@nb.njit
def gpf(n: int=1 << 20) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n - 1:
    i += 1
    if s[i] == i: s[i::i] = i
  return s


@nb.njit
def prime_factor_cnt(n: int) -> np.ndarray:
  pn = prime_numbers(n)
  cnt = np.zeros(n, np.int64)
  for p in pn: cnt[p::p] += 1
  return cnt


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, k: int) -> typing.NoReturn:
  cnt = prime_factor_cnt(n + 1)
  print(np.count_nonzero(cnt >= k))



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
