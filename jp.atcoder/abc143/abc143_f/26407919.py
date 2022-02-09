import typing
import  sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  b = np.zeros(n, np.int64)
  for x in a: b[x - 1] += 1
  b.sort()
  s = np.hstack((np.array([0]), b)).cumsum()

  def binary_search(k):
    def possible(t):
      i = np.searchsorted(b, t)
      return t * (n - i) + s[i] >= t * k

    lo, hi = 0, n // k + 1
    while hi - lo > 1:
      t = (lo + hi) >> 1
      if possible(t): lo = t
      else: hi = t
    return lo

  for k in range(1, n + 1):
    t = binary_search(k)
    print(t)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
