import typing
import sys
import numpy as np


def solve(
  x: np.array,
  y: np.array,
) -> typing.NoReturn:
  n = x.size
  ord = np.argsort(x, kind='mergesort')
  x, y = x[ord], y[ord]

  mn = np.minimum.accumulate(y)
  mx = np.maximum.accumulate(y)

  def possible(d):
    j = np.searchsorted(x, x - d, 'right') - 1
    j, v = j[j >= 0], y[j >= 0]
    return np.any(
      (np.abs(mx[j] - v) >= d)
      | (np.abs(mn[j] - v) >= d),
    )

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
