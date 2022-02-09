import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def prime_factorize(
  n: int,
) -> np.array:
  prime, cnt = [], []
  i = 1
  while i * i < n:
    i += 1
    if n % i: continue
    prime.append(i)
    cnt.append(0)
    while n % i == 0:
      n //= i
      cnt[-1] += 1
  if n > 1:
    prime.append(n)
    cnt.append(1)
  return np.vstack((
    np.array(prime),
    np.array(cnt),
  )).T


@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def solve(
  a: np.array,
  m: int,
) -> typing.NoReturn:
  n = a.size

  p = np.zeros(1 << 20, dtype=np.bool8)
  for i in range(n):
    x = a[i]
    res = prime_factorize(x)
    for j in res.T[0]: p[j] = True

  s = np.ones(1 + m, dtype=np.bool8)
  s[0] = False
  for i in range(1 + m):
    if not p[i] or not s[i]: continue
    for j in range(i, 1 + m, i):
      s[j] = False
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
