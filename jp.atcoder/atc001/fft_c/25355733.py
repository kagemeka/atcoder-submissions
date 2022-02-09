import typing

import cmath
import sys
import numpy as np


def fft(
  a: typing.List[int],
  inverse: bool=False,
) -> typing.List[int]:
  n = len(a)
  h = n.bit_length() - 1

  for i in range(n):
    j = 0
    for k in range(h):
      j |= (i >> k & 1) << (h - 1 - k)
    if i < j: a[i], a[j] = a[j], a[i]

  b = 1
  sign = -1 + 2 * inverse
  while b < n:
    for j in range(b):
      w = cmath.rect(
        1.,
        sign * cmath.pi / b * j,
      )
      k = 0
      while k < n:
        s = a[k + j]
        t = a[k + j + b] * w
        a[k + j] = s + t
        a[k + j + b] = s - t
        k += 2 * b
    b <<= 1

  if inverse:
    for i in range(n): a[i] /= n

  return a



class FFT():
  def __butterfly(
    self,
  ) -> typing.NoReturn:
    n = self.__n
    a = self.__a
    b = 1
    sign= -1 + 2 * self.__inv
    while b < n:
      j = np.arange(b)
      w = np.exp(sign * np.pi / b * j * 1j)
      k = np.arange(0, n, 2 * b)[:, None]
      s, t = a[k + j], a[k + j + b] * w
      a[k + j], a[k + j + b] = s + t, s - t
      b <<= 1


  def __call__(
    self,
    a: np.ndarray,
  ) -> np.ndarray:
    self.__a = a.astype(np.complex128)
    n = a.size
    h = n.bit_length() - 1
    self.__n, self.__h = n, h
    self.__reverse_bits()
    self.__butterfly()
    a = self.__a
    if self.__inv: a /= n
    return a


  def __init__(
    self,
    inverse: bool=False,
  ) -> typing.NoReturn:
    self.__inv = inverse


  def __reverse_bits(
    self,
  ) -> typing.NoReturn:
    i = np.arange(self.__n)
    h = self.__h
    bits = i[:, None] >> np.arange(h) & 1
    j = (bits[:, ::-1] * (1 << np.arange(h))).sum(axis=1)
    self.__a = self.__a[j]



def solve(
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  n = a.size
  m = 1 << 18
  a = np.pad(a, (1, m - n - 1))
  b = np.pad(b, (1, m - n - 1))
  a = a.astype(np.complex128)
  b = b.astype(np.complex128)
  fft = FFT()
  ifft = FFT(inverse=True)
  a = fft(a)
  b = fft(b)
  c = a * b
  c = ifft(c)
  c = np.around(np.real(c)).astype(int)
  print(*c[1:2 * n + 1], sep='\n')



def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  solve(a, b)


main()
