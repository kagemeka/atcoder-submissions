import typing
import sys
import numpy as np
import numba as nb




def to_ufunc(nin: int, nout: int) -> typing.Callable:
  def wrap(f: typing.Callable) -> typing.Callable:
    return np.frompyfunc(f, nin, nout)
  return wrap


@to_ufunc(2, 1)
def minimum(x: np.ndarray, y: np.ndarray):
  return np.minimum(x + 1, y)


def rotate_matrix_90(a: np.ndarray) -> np.ndarray:
  return a.T[::-1]

def solve(grid: np.ndarray, k: int) -> typing.NoReturn:
  h, w = grid.shape
  inf = 1 << 10
  a = np.zeros((h + 2, w + 2), np.int64)
  a[1:h + 1, 1:w + 1][grid == 1] = inf
  for _ in range(4):
    minimum.accumulate(a, axis=0, out=a, dtype=np.object0)
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
