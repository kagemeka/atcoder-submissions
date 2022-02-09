import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ), cache=True)
def uf_build(n: int) -> np.ndarray:
  return np.full(n, -1, np.int64)


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



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = a.size
  uf = uf_build(1 << 18)
  cnt = 0
  for i in range(n // 2):
    x, y = a[i], a[n - 1 - i]
    x, y = uf_find(uf, x), uf_find(uf, y)
    if x == y: continue
    uf_unite(uf, x, y)
    cnt += 1
  print(cnt)




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
