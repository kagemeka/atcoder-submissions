import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:], nb.i8), cache=True)
def solve(
  l: int,
  a: np.ndarray,
  k: int,
) -> typing.NoReturn:
  n = a.size
  a = np.hstack((a, np.array([l])))

  def possible(x):
    cnt = 0
    s = 0
    for v in a:
      if v - s < x: continue
      s = v
      cnt += 1
    return cnt >= k + 1


  def binary_search():
    lo, hi = 0, 1 << 30
    while hi - lo > 1:
      x = (lo + hi) // 2
      if possible(x):
        lo = x
      else:
        hi = x
    return lo


  print(binary_search())


def main() -> typing.NoReturn:
  n, l = map(int, input().split())
  k = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(l, a, k)


main()
