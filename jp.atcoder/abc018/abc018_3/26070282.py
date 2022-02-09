import typing
import sys
import numpy as np
import numba as nb


def rotate_matrix_90(a: np.ndarray) -> np.ndarray:
  return a.T[::-1]

def solve(grid: np.ndarray, k: int) -> typing.NoReturn:
  h, w = grid.shape
  inf = 1 << 10
  a = np.zeros((h + 2, w + 2), np.int64)
  a[1:h + 1, 1:w + 1][grid == 1] = inf
  for _ in range(4):
    for i in range(len(a) - 1):
      np.minimum(a[i + 1], a[i] + 1, out=a[i + 1])
    a = rotate_matrix_90(a)
  print(np.count_nonzero(a >= k))


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
