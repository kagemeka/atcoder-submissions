import typing

import cmath
import sys
import numpy as np







def fft(
  a: typing.List[int],
  inverse: bool=False,
) -> typing.List[int]:
  ...
  n = len(a)
  h = n.bit_length() - 1

  # swap initializing
  for i in range(n):
    j = 0
    for k in range(h):
      j |= (i >> k & 1) << (h - 1 - k)
    if i < j: a[i], a[j] = a[j], a[i]


  # butterfly
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



def solve(
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  n = a.size
  m = 1 << 4
  a = np.pad(a, (1, m - n - 1))
  b = np.pad(b, (1, m - n - 1))
  a = a.astype(np.complex128)
  b = b.astype(np.complex128)
  a = list(a)
  b = list(b)
  a = fft(a)
  b = fft(b)
  # c = a * b
  c = [a[i] * b[i] for i in range(m)]
  c = fft(c, inverse=1)
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
