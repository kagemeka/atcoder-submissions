import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(
  a: np.ndarray,
  k: int,
) -> typing.NoReturn:
  n = len(a)


  def possible(x):
    cnt = (a + x - 1) // x - 1
    return cnt.sum() <= k


  def binary_search():
    lo, hi = 0, 1 << 30
    while hi - lo > 1:
      x = (lo + hi) // 2
      if possible(x):
        hi = x
      else:
        lo = x
    return hi

  print(binary_search())



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
