import typing
import sys
import numpy as np
import numba as nb
import scipy.ndimage


def solve(grid: np.ndarray, k: int) -> typing.NoReturn:
  a = np.pad(grid, pad_width=1, constant_values=0)
  cdt = scipy.ndimage.distance_transform_cdt(
    input=a,
    metric='taxicab',
  )
  print(np.count_nonzero(cdt >= k))


def main() -> typing.NoReturn:
  readline = sys.stdin.buffer.readline
  read = sys.stdin.buffer.read

  h, w, k = map(int, readline().split())
  s = np.frombuffer(
    read(),
    dtype='S1',
  ).reshape(h, w + 1)[:, :-1]
  grid = np.zeros((h, w), np.int64)
  grid[s == b'o'] = 1
  solve(grid, k)


main()
