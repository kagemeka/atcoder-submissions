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
  h = 1
  while 1 << h < n: h += 1
  assert 1 << h == n

  def _reverse_bits():
    idx = np.empty(n, dtype=np.int32)
    for i in range(n):
      j = 0
      for k in range(h):
        j |= (i >> k & 1) << (h - 1 - k)
      idx[i] = j
    nonlocal a
    a = a[idx]

  def _butterfly():
    sign = -1 + 2 * inverse
    b = 1
    while b < n:
      for j in range(b):
        w = np.exp(sign * np.pi / b * j * 1j)
        for k in range(0, n, 2 * b):
          s, t = a[k + j], a[k + j + b] * w
          a[k + j], a[k + j + b] = s + t, s - t
      b <<= 1

  _reverse_bits()
  _butterfly()
  if inverse: a /= n
  return a


@nb.njit
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
  c = fft(a * b, inverse=True)[:n]
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
