import typing
import sys
import numpy as np
import numba as nb





@nb.njit((nb.c16[:], nb.optional(nb.b1)))
def fft(
  a: np.ndarray,
  inverse: bool=False
) -> np.ndarray:
  n = a.size
  if n == 1: return a
  h = 1
  while 1 << h < n: h += 1
  assert 1 << h == n

  b = fft(a[::2], inverse)
  c = fft(a[1::2], inverse)

  a = np.zeros(n, dtype=np.complex128)
  sign = -1 + 2 * inverse
  zeta = np.exp(sign * 2j * np.pi / n * np.arange(n))
  m = n // 2
  a[:m] = a[m:] = c
  a *= zeta
  a[:m] += b; a[m:] += b
  return a


@nb.njit((nb.c16[:], ))
def ifft(
  a: np.ndarray,
) -> np.ndarray:
  return fft(a, inverse=True) / a.size



@nb.njit((nb.i8[:], nb.i8[:]))
def convolve(
  a: np.ndarray,
  b: np.ndarray,
) -> np.ndarray:
  n = a.size + b.size - 1
  m = 1
  while m < n: m <<= 1
  na = np.zeros(m, dtype=np.complex128)
  nb = np.zeros(m, dtype=np.complex128)
  na[:a.size] = a
  nb[:b.size] = b
  a, b = na, nb
  a = fft(a, inverse=False)
  b = fft(b, inverse=False)
  c = a * b
  c = ifft(c)[:n]
  c = np.rint(np.real(c)).astype(np.int64)
  return c


@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  a: np.ndarray,
  b: np.ndarray,
) -> typing.NoReturn:
  a = np.hstack((np.array([0]), a))
  b = np.hstack((np.array([0]), b))
  c = convolve(a, b)
  n = a.size
  for x in c[1:2 * n + 1]:
    print(x)


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  solve(a, b)


main()
