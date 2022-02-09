import typing
import sys
import numpy as np
from scipy import signal


def mod_convolve(
  f: np.ndarray,
  g: np.ndarray,
  mod: int,
) -> np.ndarray:
  N = 15
  BASE = 1 << N
  f1, f0 = np.divmod(f, BASE)
  g1, g0 = np.divmod(g, BASE)
  a = signal.fftconvolve(f1, g1)
  c = signal.fftconvolve(f0, g0)
  a = np.rint(a).astype(np.int64) % mod
  c = np.rint(c).astype(np.int64) % mod
  b = signal.fftconvolve(f0 + f1, g0 + g1)
  b = np.rint(b).astype(np.int64) % mod
  b = (b - a - c) % mod
  h = (a << N * 2) + (b << N) + c
  return h % mod


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
  print(*mod_convolve(a, b, mod))


main()
