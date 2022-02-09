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


  def heuristic_func(y, x):
    return abs(gy - y) + abs(gx - x)

  def is_goal(y, x):
    return y == gy and x == gx


  def a_star_shortest_dist(t2):
    dist = np.full((h, w), inf, np.int64)
    dist[sy, sx] = 0
    hs = heuristic_func(sy, sx)
    hq = [(hs, hs, sy, sx)]
    dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))
    while hq:
      su, hu, y, x = heapq.heappop(hq)
      du = su - hu
      if du > dist[y, x]: continue
      if is_goal(y, x): return dist[y, x]
      for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not on_grid(ny, nx): continue
        dv = du + (t2 if grid[ny, nx] else 1)
        if dv >= dist[ny, nx]: continue
        dist[ny, nx] = dv
        hv = heuristic_func(ny, nx)
        heapq.heappush(hq, (hv + dv, hv, ny, nx))


  def possible(x):
    return a_star_shortest_dist(x) <= t

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
