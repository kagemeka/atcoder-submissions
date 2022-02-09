import typing
import numpy as np
import numba as nb



@nb.njit
def find(
  a: np.array,
  u: int,
) -> int:
  pu = a[u]
  if pu < 0: return u
  pu = find(a, pu)
  a[u] = pu
  return pu


@nb.njit
def unite(
  a: np.array,
  u: int,
  v: int,
) -> typing.NoReturn:
  u = find(a, u)
  v = find(a, v)
  if u == v: return
  if a[u] > a[v]: u, v = v, u
  a[u] += a[v]
  a[v] = u



@nb.njit(cache=True)
def solve(
  n: int,
  q: np.array,
) -> typing.NoReturn:
  ps = np.full(n, -1, np.int64)
  for t, u, v in q:
    if t == 0:
      unite(ps, u, v)
    else:
      u = find(ps, u)
      v = find(ps, v)
      print((u == v) * 1)


import sys

def main() -> typing.NoReturn:
  n, q = map(
    int, input().split(),
  )
  q = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(q, 3)
  solve(n, q)


main()
