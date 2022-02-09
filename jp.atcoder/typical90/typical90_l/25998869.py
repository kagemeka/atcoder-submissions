import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def uf_build(n: int) -> np.ndarray:
  return np.full(n, -1, np.int64)


@nb.njit
def uf_find(uf: np.ndarray, u: int) -> int:
  if uf[u] < 0: return u
  uf[u] = uf_find(uf, uf[u])
  return uf[u]


@nb.njit
def uf_unite(
  uf: np.ndarray,
  u: int,
  v: int,
) -> typing.NoReturn:
  u, v = uf_find(uf, u), uf_find(uf, v)
  if u == v: return
  if uf[u] > uf[v]: u, v = v, u
  uf[u] += uf[v]
  uf[v] = u


@nb.njit((nb.i8, nb.i8, nb.i8[:]), cache=True)
def solve(
  h: int,
  w: int,
  q: np.ndarray,
) -> typing.NoReturn:
  n = h * w
  uf = uf_build(n)

  def to_1d(y, x):
    return y * w + x

  def on_grid(y, x):
    return 0 <= y < h and 0 <= x < w

  is_red = np.zeros(n, np.bool8)

  dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))

  while q.size:
    if q[0] == 0:
      y, x = q[1:3]
      q = q[3:]
      u = to_1d(y, x)
      is_red[u] = True
      for i in range(4):
        dy, dx = dyx[i]
        ny, nx = y + dy, x + dx
        if not on_grid(ny, nx): continue
        v = to_1d(ny, nx)
        if is_red[v]: uf_unite(uf, u, v)
    else:
      y0, x0, y1, x1 = q[1:5]
      q = q[5:]
      u = to_1d(y0, x0)
      v = to_1d(y1, x1)
      same = uf_find(uf, u) == uf_find(uf, v)
      ans = 'Yes' if same and is_red[u] else 'No'
      print(ans)




def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  q = int(input())
  q = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ) - 1
  solve(h, w, q)


main()
