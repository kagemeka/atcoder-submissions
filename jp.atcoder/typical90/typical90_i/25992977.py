import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
  n = len(xy)
  mx = 0

  def calc_max(deg):
    eps = 1e-7
    deg = np.hstack((deg, deg + 360))
    k = 0
    mx = 0
    for i in range(n - 1):
      while k < i + n - 1 and deg[k + 1] - deg[i] < 180 + eps:
        k += 1
      mx = max(mx, deg[k] - deg[i])
    return mx

  for j in range(n):
    cx, cy = xy[j]
    px, py = xy[np.arange(n) != j].T
    rad = np.arctan2(py - cy, px - cx)
    deg = np.rad2deg(rad)
    deg[deg < 0] += 360
    deg.sort()
    mx = max(mx, calc_max(deg))
  print(mx)

def main() -> typing.NoReturn:
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy)


main()
