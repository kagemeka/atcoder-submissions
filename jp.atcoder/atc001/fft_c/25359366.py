import typing
import sys
import cmath


class FFT():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    self.__dft(a)
    n = len(a)
    if self.__inv:
      for i in range(n): a[i] /= n



  def __dft(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    n = len(a)
    if n == 1: return
    m = n // 2
    b = [0] * m
    c = [0] * m
    for i in range(m):
      b[i] = a[2 * i]
      c[i] = a[2 * i + 1]
    self.__dft(b)
    self.__dft(c)
    sign = -1 + 2 * self.__inv
    zeta = cmath.rect(1, sign * 2 * cmath.pi / n)
    x = 1
    for i in range(n):
      a[i] = b[i % m] + x * c[i % m]
      x *= zeta


  def __init__(
    self,
    inverse: bool=False
  ) -> typing.NoReturn:
    self.__inv = inverse



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
