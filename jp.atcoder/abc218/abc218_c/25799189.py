import typing
import sys
import numpy as np


def rotate_right(grid: np.ndarray) -> np.ndarray:
  return grid[::-1].T


def trim(g: np.ndarray) -> np.ndarray:
  for _ in range(4):
    while not np.any(g[0]):
      g = g[1:]
    g = rotate_right(g)
  return g


def solve(
  grid: np.ndarray,
) -> typing.NoReturn:
  n = len(grid) // 2
  s, t = grid[:n], grid[n:]
  s, t = trim(s), trim(t)
  for _ in range(n):
    t = rotate_right(t)
    if s.shape != t.shape: continue
    if not np.all(s == t): continue
    print('Yes')
    return
  print('No')


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  grid = np.frombuffer(
    sys.stdin.buffer.read(),
    dtype='S1',
  ).reshape(n * 2, -1)[:, :-1] == b'#'
  solve(grid)


main()
