import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit((nb.b1[:, :], ) + (nb.i8, ) * 5, cache=True)
def solve(
  grid: np.ndarray,
  sy: int,
  sx: int,
  gy: int,
  gx: int,
  t: int,
) -> typing.NoReturn:
  h, w = grid.shape
  inf = 1 << 60

  def on_grid(y, x):
    return 0 <= y < h and 0 <= x < w

  def possible(t2):
    dist = np.full((h, w), inf, np.int64)
    dist[sy, sx] = 0
    hq = [(0, sy, sx)]
    dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))
    while hq:
      du, y, x = heapq.heappop(hq)
      for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not on_grid(ny, nx): continue
        dv = du + (t2 if grid[ny, nx] else 1)
        if dv >= dist[ny, nx]: continue
        dist[ny, nx] = dv
        heapq.heappush(hq, (dv, ny, nx))
    return dist[gy, gx] <= t

  def binary_search():
    lo, hi = 1, 1 << 30
    while hi - lo > 1:
      x = (lo + hi) // 2
      if possible(x):
        lo = x
      else:
        hi = x
    return lo

  print(binary_search())


def main() -> typing.NoReturn:
  read = sys.stdin.buffer.read
  readline = sys.stdin.buffer.readline
  h, w, t = map(int, readline().split())
  s = np.frombuffer(
    read(),
    dtype='S1',
  ).reshape(h, w + 1)[:, :-1]
  grid = np.zeros((h, w), np.bool8)
  grid[s == b'#'] = True
  sy, sx = np.argwhere(s == b'S')[0]
  gy, gx = np.argwhere(s == b'G')[0]
  solve(grid, sy, sx, gy, gx, t)


main()
