import typing
import sys
import numpy as np
from numba import njit, i8, b1



@njit(
  (i8, i8, b1[:, :]),
  cache=True,
)
def solve(
  h: int,
  w: int,
  g: np.array,
) -> typing.NoReturn:

  inf = 1 << 30
  dist = np.full(
    (h, w),
    inf,
    dtype=np.int64,
  )
  dist[0, 0] = 0


  dij = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
  )

  def on_grid(u):
    i, j = u
    return (
      0 <= i < h and
      0 <= j < w
    )

  q = np.empty(
    (1 << 20, 2),
    dtype=np.int64,
  )
  l, r = 0, -1
  r += 1
  q[r] = (0, 0)
  while l <= r:
    (i, j) = q[l]
    l += 1
    u = (i, j)
    du = dist[u]
    for k in range(len(dij)):
      di, dj = dij[k]
      v = (i + di, j + dj)
      if not on_grid(v):
        continue
      if not g[v]: continue
      dv = du
      if dv >= dist[v]:
        continue
      dist[v] = dv
      l -= 1
      q[l] = v

    for di in range(-2, 3):
      for dj in range(-2, 3):
        md = abs(di) + abs(dj)
        if md == 4 or md == 0:
          continue
        v = (i + di, j + dj)
        if not on_grid(v):
          continue
        dv = du + 1
        if dv >= dist[v]:
          continue
        dist[v] = dv
        r += 1
        q[r] = v
  print(dist[-1, -1])



def main() -> typing.NoReturn:
  h, w = np.fromstring(
    sys.stdin.buffer
    .readline().decode(),
    dtype=np.int64,
    sep=' ',
  )
  s = b''.join(
    sys.stdin.buffer
    .read().split(),
  )
  g = np.frombuffer(
    s,
    dtype='S1',
  ).reshape(h, w) != b'#'
  solve(h, w, g)


main()
