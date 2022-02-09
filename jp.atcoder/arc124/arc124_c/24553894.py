import typing
import numpy as np
import sys


def divisors(
  n: int,
) -> np.array:
  i = 1
  a = []
  while i * i < n:
    if n % i:
      i += 1
      continue
    a.append(i)
    a.append(n // i)
    i += 1
  if i * i == n: a.append(i)
  a = np.array(a)
  a.sort()
  return a
  # i = np.sqrt(n).astype(int)
  # i = np.arange(1, i + 1)
  # i = i[n % i == 0]
  # d = np.hstack([i, n // i])
  # return np.unique(d)


def solve(
  n: int,
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  d1 = divisors(a[0])
  d2 = divisors(b[0])
  d1, d2 = np.meshgrid(d1, d2)
  d1 = d1.ravel()
  d2 = d2.ravel()
  d = np.vstack((d1, d2)).T
  l = np.lcm(d[:, 0], d[:, 1])
  d = d[..., None]
  a = a % d == 0
  b = b % d == 0
  ok = (a & b[:, ::-1]).any(
    axis=1,
  ).all(axis=-1)
  print(l[ok].max())


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  solve(n, a, b)


main()
