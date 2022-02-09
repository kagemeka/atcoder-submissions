import typing
import sys
sys.setrecursionlimit(1 << 20)
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def uf_find(uf: np.ndarray, u: int) -> int:
  if uf[u] < 0: return u
  uf[u] = uf_find(uf, uf[u])
  return uf[u]


@nb.njit((nb.i8[:], nb.i8, nb.i8), cache=True)
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


@nb.njit((nb.i8[:, :],), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  assert a.shape == (n, n)

  g = np.empty((64, 2), np.int64)
  idx_to_add = 0
  def add_edge(u, v):
    nonlocal idx_to_add
    g[idx_to_add] = (u, v)
    idx_to_add += 1

  def to_1d(y, x):
    return y * n + x

  dyx = [(0, -1), (-1, 0), (1, 0), (0, 1)]
  for i in range(n):
    for j in range(n):
      u = to_1d(i, j)
      for k in range(4):
        dy, dx = dyx[k]
        ni, nj = i + dy, j + dx
        if ni < 0 or ni > n - 1 or nj < 0 or nj > n - 1:
          continue
        add_edge(u, to_1d(ni, nj))

  g = g[:idx_to_add]


  t = 0
  for i in range(n):
    for j in range(n):
      if a[i, j] == 0: continue
      t |= 1 << to_1d(i, j)


  def check_ok(s):
    def contain_all_target():
      return t & ~s == 0


    def connected():
      uf = np.full(n * n, -1, np.int64)
      for i in range(len(g)):
        u, v = g[i]
        if ~s >> u & 1 or ~s >> v & 1: continue
        uf_unite(uf, u, v)
      root = np.empty(n * n, np.int64)
      selected = np.zeros(n * n, np.bool8)
      for i in range(n * n):
        root[i] = uf_find(uf, i)
        selected[i] = s >> i & 1
      root = root[selected]
      return np.all(root[:-1] == root[1:])


    def all_open():
      open_ = np.ones(n * n, np.bool8)
      b = np.array([5, 6, 9, 10])
      open_[b] = False
      for i in b:
        if s >> i & 1:
          open_[i] = True
          continue
        que = [i]
        visited = np.zeros(n * n, np.bool8)
        visited[i] = True
        for i in que:
          y, x = divmod(i, n)
          for k in range(4):
            dy, dx = dyx[k]
            ny, nx = y + dy, x + dx
            if ny < 0 or ny > n - 1 or nx < 0 or nx > n - 1:
              continue
            j = to_1d(ny, nx)
            if s >> j & 1: continue
            if visited[j]: continue
            visited[j] = True
            open_[i] |= open_[j]
            open_[j] |= open_[i]
            que.append(j)
      return np.all(open_[b])

    return contain_all_target() and connected() and all_open()


  cnt = 0
  for s in range(1 << (n * n)):
    cnt += check_ok(s)
  print(cnt)


def main() -> typing.NoReturn:
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(4, 4)
  solve(a)



main()
