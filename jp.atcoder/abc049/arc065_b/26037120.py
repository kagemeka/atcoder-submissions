import typing
import  sys
import numpy as np
import numba as nb


@nb.njit
def uf_build(n: int) -> np.ndarray:
  return np.full(n, -1, np.int64)


@nb.njit
def uf_find(uf: np.ndarray, u:int) -> int:
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


@nb.njit
def connected_components(n: int, g: np.ndarray) -> np.ndarray:
  uf = uf_build(n)
  m = len(g)
  for i in range(m):
    u, v = g[i, :2]
    uf_unite(uf, u, v)
  label = np.empty(n, np.int64)
  for i in range(n):
    label[i] = uf_find(uf, i)
  return label


@nb.njit
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v


@nb.njit((nb.i8, nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(
  n: int,
  pq: np.ndarray,
  rs: np.ndarray,
) -> typing.NoReturn:
  k, l = len(pq), len(rs)
  label0 = connected_components(n, pq)
  label1 = connected_components(n, rs)
  label = label0 * (1 << 17) + label1
  label, _ = compress_array(label)
  b = np.bincount(label)
  cnt = b[label]
  for c in cnt:
    print(c)


def main() -> typing.NoReturn:
  n, k, l = map(int, input().split())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(-1, 2) - 1
  pq = I[:k]
  rs = I[k:]
  solve(n, pq, rs)


main()
