import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def rotate_matrix_90(a: np.ndarray) -> np.ndarray:
  return a.copy().T[::-1]


@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def solve(grid: np.ndarray, k: int) -> typing.NoReturn:
  h, w = grid.shape
  inf = 1 << 10
  a = np.zeros((h + 2, w + 2), np.int64)
  for i in range(h):
    for j in range(w):
      if grid[i, j] == 0: continue
      a[i + 1, j + 1] = inf

  def cummin(a):
    for i in range(a.shape[0] - 1):
      for j in range(a.shape[1]):
        a[i + 1, j] = min(a[i + 1, j], a[i, j] + 1)

  for _ in range(4):
    cummin(a)
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
