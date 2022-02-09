import typing
import sys
import numpy as np


def solve(
  h: int,
  w: int,
  yx: np.ndarray,
  k: int,
) -> typing.NoReturn:
  y, x = yx.T

  bin_y = np.bincount(y)
  bin_x = np.bincount(x)
  bin2_y = np.bincount(bin_y, minlength=k + 1)
  bin2_x = np.bincount(bin_x, minlength=k + 1)
  tot = np.sum(bin2_y[:k + 1] * bin2_x[k::-1])
  real = np.bincount(bin_y[y] + bin_x[x] - 1, minlength=k + 1)
  tot += real[k] - real[k - 1]
  print(tot)



def main() -> typing.NoReturn:
  h, w, k = map(int, input().split())
  n = int(input())
  yx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2) - 1
  solve(h, w, yx, k)


main()
