import typing
import sys
import numpy as np



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
    (1 << 20, 3),
    dtype=np.int64,
  )
  qn = 0
  def swap(i, j):
    tmp = q[i].copy()
    q[i] = q[j]
    q[j] = tmp


  def push(x):
    i = qn
    q[i] = x
    while i > 0:
      j = (i - 1) // 2
      if q[i][0] >= q[j][0]:
        break
      swap(i, j)
      i = j


  def pop():
    n = qn - 1
    swap(0, n)
    i = 0
    while 1:
      j = i * 2 + 1
      if j >= n: break
      dj = q[j, 0]
      if j < n - 1:
        j += q[j + 1][0] < q[j][0]
      dj = q[j][0]
      if q[i][0] <= dj: break
      swap(i, j)
      i = j
    return q[n]

  push((0, 0, 0))
  qn += 1

  while qn:
    (du, i, j) = pop()
    qn -= 1
    u = (i, j)
    if du > dist[u]:
      continue
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
      push((dv, *v))
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
        push((dv, *v))
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


OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import i8, b1
  from numba.pycc import CC
  cc = CC('my_module')
  fn = solve
  sig = (i8, i8, b1[:, :])
  cc.export(
    fn.__name__,
    sig,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
