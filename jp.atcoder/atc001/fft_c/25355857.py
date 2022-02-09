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
    sign = -1 + 2 * self.__inv
    while b < n:
      for j in range(b):
        w = cmath.rect(1., sign * cmath.pi / b * j)
        k = 0
        while k < n:
          s, t = a[k + j], a[k + j + b] * w
          a[k + j], a[k + j + b] = s + t, s - t
          k += 2 * b
      b <<= 1


  def __call__(
    self,
    a: typing.List[complex],
  ) -> typing.List[complex]:
    n = len(a)
    h = n.bit_length() - 1
    self.__a = a
    self.__n, self.__h = n, h
    self.__reverse_bits()
    self.__butterfly()
    a = self.__a
    if self.__inv:
      for i in range(n): a[i] /= n
    return a


  def __init__(
    self,
    inverse: bool=False,
  ) -> typing.NoReturn:
    self.__inv = inverse


  def __reverse_bits(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    n, h = self.__n, self.__h
    idx = [-1] * n
    for i in range(n):
      j = 0
      for k in range(h):
        j |= (i >> k & 1) << (h - 1 - k)
      idx[i] = j
    self.__a = [a[i] for i in idx]



def solve(
  a: typing.List[int],
  b: typing.List[int],
) -> typing.NoReturn:
  n = len(a)
  m = 1 << 18
  a += [0] * (m - n)
  b += [0] * (m - n)
  fft = FFT()
  ifft = FFT(inverse=True)
  a = fft(a)
  b = fft(b)
  c = [a[i] * b[i] for i in range(m)]
  c = ifft(c)
  c = [int(round(x.real)) for x in c]
  print(*c[1:2 * n - 1], sep='\n')



def main() -> typing.NoReturn:
  n = int(input())
  a = [0] * (n + 1)
  b = [0] * (n + 1)
  for i in range(n):
    a[i + 1], b[i + 1] = map(int, input().split())
  solve(a, b)


main()
