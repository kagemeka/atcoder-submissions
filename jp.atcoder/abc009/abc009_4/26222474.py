import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def matrix_identity(n: int) -> np.ndarray:
  and_e = (1 << 63) - 1
  e = np.zeros((n, n), np.int64)
  for i in range(n): e[i, i] = and_e
  return e


@nb.njit
def matrix_dot(a: np.ndarray, b: np.ndarray) -> np.ndarray:
  n, m = a.shape
  h, w = b.shape
  assert m == h
  c = np.zeros((n, w), np.int64)
  for i in range(n):
    for j in range(w):
      for k in range(m):
        c[i, j] ^= a[i, k] & b[k, j]
  return c



@nb.njit
def matrix_power(a: np.ndarray, n: int) -> np.ndarray:
  b = matrix_identity(len(a))
  while n:
    if n & 1: b = matrix_dot(b, a)
    a = matrix_dot(a, a)
    n >>= 1
  return b



@nb.njit((nb.i8[:], nb.i8[:], nb.i8), cache=True)
def solve(
  a: np.ndarray,
  c: np.ndarray,
  k: int,
) -> typing.NoReturn:
  n = len(a)
  if k <= n:
    print(a[k - 1])
    return
  b = np.empty((n, 1), np.int64)
  for i in range(n): b[-i - 1, 0] = a[i]
  d = np.eye(n, n, -1, np.int64)
  and_e = (1 << 63) - 1
  d *= and_e
  d[0] = c
  d = matrix_power(d, k - n)
  b = matrix_dot(d, b)
  print(b[0, 0])


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, c, k)


main()
