import typing
import sys
# import numpy as np



# class FFT():
#   def __butterfly(
#     self,
#   ) -> typing.NoReturn:
#     n = self.__n
#     a = self.__a
#     b = 1
#     sign= -1 + 2 * self.__inv
#     while b < n:
#       j = np.arange(b)
#       w = np.exp(sign * np.pi / b * j * 1j)
#       k = np.arange(0, n, 2 * b)[:, None]
#       s, t = a[k + j], a[k + j + b] * w
#       a[k + j], a[k + j + b] = s + t, s - t
#       b <<= 1


#   def __call__(
#     self,
#     a: np.ndarray,
#   ) -> np.ndarray:
#     self.__a = a.astype(np.complex128)
#     n = a.size
#     h = n.bit_length() - 1
#     self.__n, self.__h = n, h
#     self.__reverse_bits()
#     self.__butterfly()
#     a = self.__a
#     if self.__inv: a /= n
#     return a


#   def __init__(
#     self,
#     inverse: bool=False,
#   ) -> typing.NoReturn:
#     self.__inv = inverse


#   def __reverse_bits(
#     self,
#   ) -> typing.NoReturn:
#     i = np.arange(self.__n)
#     h = self.__h
#     bits = i[:, None] >> np.arange(h) & 1
#     j = (bits[:, ::-1] * (1 << np.arange(h))).sum(axis=1)
#     self.__a = self.__a[j]


import cmath

def fft(
  a: typing.List[int],
  inverse: bool=False,
) -> typing.NoReturn:
  n = len(a)
  if n == 1: return
  m = n // 2
  b = [0] * m
  c = [0] * m
  for i in range(m):
    b[i] = a[2 * i]
    c[i] = a[2 * i + 1]
  fft(b, inverse)
  fft(c, inverse)
  sign = -1 + 2 * inverse
  zeta = cmath.rect(1, sign * 2 * cmath.pi / n)
  x = 1
  for i in range(n):
    a[i] = b[i % m] + x * c[i % m]
    x *= zeta



def ifft(
  a: typing.List[int],
) -> typing.NoReturn:
  fft(a, inverse=1)
  for i in range(len(a)):
    a[i] /= len(a)




def solve(
  a: typing.List[int],
  b: typing.List[int],
) -> typing.NoReturn:
  n = len(a)
  m = 1 << 18
  a += [0] * (m - n)
  b += [0] * (m - n)
  fft(a)
  fft(b)
  c = [a[i] * b[i] for i in range(m)]
  ifft(c)
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
