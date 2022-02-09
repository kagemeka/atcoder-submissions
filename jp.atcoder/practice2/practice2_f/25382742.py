import typing
import sys
import numpy as np
from scipy import signal


class ModConvolve():
  def __call__(
    self,
    f: np.ndarray,
    g: np.ndarray,
  ) -> np.ndarray:
    mod = self.__mod
    N: typing.Final[int] = 10
    BASE: typing.Final[int] = 1 << N
    f, f0 = np.divmod(f, BASE)
    f2, f1 = np.divmod(f, BASE)
    g, g0 = np.divmod(g, BASE)
    g2, g1 = np.divmod(g, BASE)
    h0 = self.__conv(f0, g0)
    ha = self.__conv(f1, g1)
    h4 = self.__conv(f2, g2)
    h1 = self.__conv(f0 + f1, g0 + g1) - h0 - ha
    h3 = self.__conv(f1 + f2, g1 + g2) - ha - h4
    h2 = self.__conv(f0 + f2, g0 + g2) - h0 - h4 + ha
    h = (h4 << N * 2) + (h3 << N) + h2
    h = (h % mod << N * 2) + (h1 << N) + h0
    return h % mod


  def __conv(
    self,
    f: np.ndarray,
    g: np.ndarray,
  ) -> np.ndarray:
    h = signal.fftconvolve(f, g)
    return np.rint(h).astype(np.int64) % self.__mod


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod

  def __conv(
    self,
    f: np.ndarray,
    g: np.ndarray,
  ) -> np.ndarray:
    h = signal.fftconvolve(f, g)
    return np.rint(h).astype(np.int64) % self.__mod


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod


mod = 998_244_353


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  convolve = ModConvolve(mod)

  print(*convolve(a, b))


main()
