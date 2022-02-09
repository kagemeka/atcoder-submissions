import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  x: np.array,
  y: np.array,
) -> typing.NoReturn:
  n = x.size
  ord = np.argsort(x, kind='mergesort')
  x, y = x[ord], y[ord]

  mn, mx = y.copy(), y.copy()
  for i in range(1, n):
    mn[i] = min(mn[i], mn[i - 1])
    mx[i] = max(mn[i], mx[i - 1])

  def possible(d):
    for i in range(n):
      j = np.searchsorted(x, x[i] - d, 'right') - 1
      if j < 0: continue
      if abs(mx[j] - y[i]) >= d or abs(mn[j] - y[i]) >= d:
        return True
    return False

  def binary_search():
    lo, hi = 0, 1 << 40
    while hi - lo > 1:
      d = (lo + hi) // 2
      if possible(d):
        lo = d
      else:
        hi = d
    return lo

  print(binary_search())


def main() -> typing.NoReturn:
  n = int(input())
  x, y = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  solve(x, y)


main()
