import typing
import sys
import numpy as np
import numba as nb
from numba import i8, b1



@nb.njit(
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
  qn = 0
  def swap(i, j):
    q[i], q[j] = q[j], q[i]


  def push(x):
    q[qn] = x
    i = qn
    while i > 0:
      j = (i - 1) // 2
      (ix, iy) = q[i]
      (jx, jy) = q[j]
      di = dist[(ix, iy)]
      dj = dist[(jx, jy)]
      if di >= dj: break
      swap(i, j)
      i = j


  def pop():
    swap(0, qn - 1)
    n = qn - 1
    i = 0
    while 1:
      j = i * 2 + 1
      if j >= n: break
      (ix, iy) = q[j + 1]
      (jx, jy) = q[j]
      di = dist[(ix, iy)]
      dj = dist[(jx, jy)]
      if (
        j < n - 1 and
        di < dj
      ): j += 1
      (ix, iy) = q[i]
      di = dist[(ix, iy)]
      if di <= dj: break
      swap(i, j)
      i = j
    return q[qn - 1]
    # TODO qn -= 1

  push((0, 0))
  qn += 1

  while qn:
    (i, j) = pop()
    qn -= 1
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
      push(v)
      qn += 1

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
        push(v)
        qn += 1
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
