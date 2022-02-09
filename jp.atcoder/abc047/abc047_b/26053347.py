import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(w: int, h: int, xya: np.ndarray) -> typing.NoReturn:
  n = len(xya)
  x_mn = y_mn = 0
  x_mx, y_mx = w, h
  for i in range(n):
    x, y, a = xya[i]
    if a == 1:
      x_mn = max(x_mn, x)
    elif a == 2:
      x_mx = min(x_mx, x)
    elif a == 3:
      y_mn = max(y_mn, y)
    elif a == 4:
      y_mx = min(y_mx, y)
  s = max(0, x_mx - x_mn) * max(0, y_mx - y_mn)
  print(s)


def main() -> typing.NoReturn:
  w, h, n = map(int, input().split())
  xya = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 3)
  solve(w, h, xya)


main()
