import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def uf_build(
  n: int,
) -> np.ndarray:
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



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_kruskal(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  sort_idx = np.argsort(csgraph[:, 2], kind='mergesort')
  csgraph = csgraph[sort_idx]
  uf = uf_build(n)

  edge_indices = np.zeros(m, np.int64)
  j = 0

  def add_edge(i):
    nonlocal edge_indices, j
    edge_indices[j] = i
    j += 1

  for i in range(m):
    u, v, _ = csgraph[i]
    if uf_find(uf, u) == uf_find(uf, v): continue
    uf_unite(uf, u, v)
    add_edge(i)

  return csgraph[edge_indices[:j]]


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  abc: np.ndarray,
) -> typing.NoReturn:
  mst = mst_kruskal(n, abc)
  print(abc[:, 2].sum() - mst[:, 2].sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abc[:, :2] -= 1
  solve(n, abc)


main()
