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
def prime_factorize(
  n: int,
  lpf: np.array,
) -> np.array:
  p, c = [-1], [-1]
  while n > 1:
    i = lpf[n]
    n //= i
    if p[-1] == i:
      c[-1] += 1
      continue
    p.append(i)
    c.append(1)
  return np.vstack((
    np.array(p),
    np.array(c),
  )).T[1:]


@nb.njit
def prime_factorize_factorial(
  n: int,
  lpf: np.array,
) -> np.array:
  prime, cnt = [], []
  idx = np.full(n + 1, -1, dtype=np.int32)
  for i in range(n + 1):
    for p, c in prime_factorize(i, lpf):
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

  _lpf = lpf(1 << 20)
  p = np.zeros(1 << 20, dtype=np.bool8)
  for i in range(n):
    x = a[i]
    res = prime_factorize(x, _lpf)
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
