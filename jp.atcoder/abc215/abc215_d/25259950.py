import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def sieve_of_eratosthenes(
  n: int,
) -> np.array:
  return gpf(n) == np.arange(n)


@nb.njit
def gpf(
  n: int,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n - 1:
    i += 1
    if s[i] == i: s[i::i] = i
  return s


@nb.njit
def lpf(
  n: int,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n - 1:
    i += 1
    if s[i] != i: continue
    j = np.arange(i, n, i)
    s[j[s[j] == j]] = i
  return s



@nb.njit
def prime_numbers(
  n: int=1 << 20,
) -> np.array:
  return np.flatnonzero(
    sieve_of_eratosthenes(n),
  )



@nb.njit
def prime_factorize(
  n: int,
  pn: np.array,
) -> np.array:
  p, c = [], []
  for i in pn:
    if i * i > n: break
    if n % i: continue
    p.append(i)
    c.append(0)
    while n % i == 0:
      n //= i
      c[-1] += 1
  if n > 1:
    p.append(n)
    c.append(1)
  return np.vstack((
    np.array(p),
    np.array(c),
  )).T


@nb.njit
def prime_factorize_factorial(
  n: int,
  pn: np.array,
) -> np.array:
  prime, cnt = [], []
  idx = np.full(n + 1, -1, dtype=np.int32)
  for i in range(n + 1):
    for p, c in prime_factorize(i, pn):
      i = idx[p]
      if i != -1:
        cnt[i] += c
        continue
      idx[p] = len(prime)
      prime.append(p)
      cnt.append(c)
  return np.vstack((
    np.array(prime),
    np.array(cnt),
  )).T



@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def solve(
  a: np.array,
  m: int,
) -> typing.NoReturn:
  n = a.size
  pn = prime_numbers(1 << 20)

  p = np.zeros(1 << 20, dtype=np.bool8)
  for i in range(n):
    x = a[i]
    res = prime_factorize(x, pn)
    for j in res.T[0]: p[j] = True

  s = np.ones(1 + m, dtype=np.bool8)
  s[0] = False
  for i in range(1 + m):
    if not p[i] or not s[i]: continue
    s[i::i] = False
  print(s.sum())
  for i in range(1 + m):
    if s[i]: print(i)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, m)


main()
