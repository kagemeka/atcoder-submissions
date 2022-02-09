import typing
import sys
import numpy as np


def convolve(
  a: np.ndarray,
  b: np.ndarray,
) -> np.ndarray:
  n = a.size + b.size - 1
  m = 1 << (n - 1).bit_length()
  a = np.fft.fft(a, m)
  b = np.fft.fft(b, m)
  c = np.fft.ifft(a * b)[:n]
  return np.rint(c).astype(np.int64)


def solve(
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  a = np.pad(a, (1, 0))
  b = np.pad(b, (1, 0))
  print(convolve(a, b))


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  solve(a, b)



main()
