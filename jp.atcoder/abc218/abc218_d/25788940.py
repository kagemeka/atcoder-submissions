import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[
  np.ndarray,
  np.ndarray,
]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def solve(
  xy: np.ndarray,
) -> typing.NoReturn:
  n = len(xy)
  x = xy[:, 0]
  y = xy[:, 1]
  x, _ = compress_array(x)
  y, _ = compress_array(y)
  x_max, y_max = x.max(), y.max()
  c = np.zeros((x_max + 1, y_max + 1), np.int64)
  for i in range(n): c[x[i], y[i]] = 1

  s = 0
  for i in range(n):
    for j in range(n):
      if i == j: continue
      if x[i] >= x[j] or y[i] >= y[j]: continue
      s += c[x[i], y[j]] * c[x[j], y[i]]
  print(s)


def main() -> typing.NoReturn:
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy)



main()
