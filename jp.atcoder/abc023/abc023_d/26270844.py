import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(hs: np.ndarray) -> typing.NoReturn:
  n = len(hs)
  h, s = hs[:, 0], hs[:, 1]

  def possible(h0):
    t = (h0 - h) // s
    t.sort()
    return np.all(t >= np.arange(n))


  def binary_search():
    lo, hi = 0, 1 << 50
    while hi - lo > 1:
      h0 = (lo + hi) // 2
      if possible(h0):
        hi = h0
      else:
        lo = h0
    return hi

  print(binary_search())

def main() -> typing.NoReturn:
  n = int(input())
  hs = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(hs)


main()
