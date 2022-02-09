import typing
import numpy as np
import sys



def find(
  a: np.array,
  u: int,
) -> int:
  if a[u] < 0: return u
  pu = find(a, a[u])
  a[u] = pu
  return pu


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



def solve(
  n: int,
  uvw: np.array
) -> typing.NoReturn:
  uvw = uvw[np.argsort(uvw[:, 2])]
  a = np.full(n, -1, dtype=np.int64)
  tot = 0
  for i in range(n - 1):
    u, v, w = uvw[i]
    u -= 1; v -= 1
    u = find(a, u)
    v = find(a, v)
    tot += a[u] * a[v] * w
    unite(a, u, v)
  print(tot)


def main() -> typing.NoReturn:
  n = int(input())
  uvw = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 3)
  solve(n, uvw)



OJ = 'ONLINE_JUDGE'

if sys.argv[-1] == OJ:
  import numba as nb
  from numba.pycc import CC
  cc = CC('my_module')
  find = nb.njit(find)
  unite = nb.njit(unite)
  fn = solve
  sig = (nb.i8, nb.i8[:, :])
  cc.export(
    fn.__name__,
    sig,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()
