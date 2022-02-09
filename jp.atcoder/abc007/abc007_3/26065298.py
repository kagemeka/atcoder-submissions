import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], nb.i8, nb.i8, nb.i8, nb.i8), cache=True)
def solve(
  grid: np.ndarray,
  sy: int,
  sx: int,
  gy: int,
  gx: int,
) -> typing.NoReturn:
  h, w = grid.shape

  inf = 1 << 60
  dist = np.full((h, w), inf, np.int64)
  dist[sy, sx] = 0
  que = [(sy, sx)]
  dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))

  def on_grid(y, x):
    return 0 <= y < h and 0 <= x < w

  for y, x in que:
    for dy, dx in dyx:
      ny = y + dy
      nx = x + dx
      if not on_grid(ny, nx): continue
      if grid[ny, nx] == 1: continue
      d = dist[y, x] + 1
      if d >= dist[ny, nx]: continue
      dist[ny, nx] = d
      que.append((ny, nx))

  print(dist[gy, gx])


def main() -> typing.NoReturn:
  h, w = map(int, sys.stdin.buffer.readline().split())
  sy, sx = map(int, sys.stdin.buffer.readline().split())
  gy, gx = map(int, sys.stdin.buffer.readline().split())
  sy -= 1
  sx -= 1
  gy -= 1
  gx -= 1
  c = np.frombuffer(
    sys.stdin.buffer.read(),
    dtype='S1',
  ).reshape(h, -1)[:, :-1]
  grid = np.zeros((h, w), np.int64)
  grid[c == b'#'] = 1
  solve(grid, sy, sx, gy, gx)


main()
