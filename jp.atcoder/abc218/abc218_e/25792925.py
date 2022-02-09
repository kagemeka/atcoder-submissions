import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def uf_build(n: int) -> np.ndarray:
  return np.full(n, -1, np.int64)


@nb.njit
def uf_find(
  uf: np.ndarray,
  u: int,
) -> int:
  if uf[u] < 0: return u
  uf[u] = uf_find(uf, uf[u])
  return uf[u]


@nb.njit
def uf_unite(
  uf: np.ndarray,
  u: int,
  v: int,
) -> typing.NoReturn:
  u = uf_find(uf, u)
  v = uf_find(uf, v)
  if u == v: return
  if uf[u] > uf[v]: u, v = v, u
  uf[u] += uf[v]
  uf[v] = u



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(
  n: int,
  abc: np.ndarray,
) -> typing.NoReturn:
  sort_idx = np.argsort(abc[:, 2], kind='mergesort')
  g = abc[sort_idx]
  m = len(g)
  added_edge_indices = np.zeros(m, np.int64)
  idx_to_add = 0
  def add_edge(i):
    nonlocal idx_to_add
    added_edge_indices[idx_to_add] = i
    idx_to_add += 1

  uf = uf_build(n)
  for i in range(m):
    u, v, w = g[i]
    if w >= 0 and uf_find(uf, u) == uf_find(uf, v):
      continue
    uf_unite(uf, u, v)
    add_edge(i)

  mst = g[added_edge_indices[:idx_to_add]]
  print(g[:, 2].sum() - mst[:, 2].sum())




def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abc[:, :2] -= 1
  solve(n, abc)


main()
