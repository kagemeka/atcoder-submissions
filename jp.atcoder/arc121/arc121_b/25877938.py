import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, c: np.ndarray) -> typing.NoReturn:
  n = len(a)
  r = a[c == 0]
  g = a[c == 1]
  b = a[c == 2]
  if len(r) & 1 ^ 1 and len(g) & 1 ^ 1:
    print(0)
    return

  inf = 1 << 60

  r.sort()
  g.sort()
  b.sort()
  if len(r) & 1 ^ 1:
    pass
  elif len(g) & 1 ^ 1:
    r, g = g, r
  else:
    r, b = b, r

  # odd <-> odd
  def min_odd_odd():
    a = np.hstack((np.array([-inf]), b, np.array([inf])))
    v0 = np.abs(g - a[np.searchsorted(a, g)])
    v1 = np.abs(g - a[np.searchsorted(a, g, side='right') - 1])
    v0[v1 < v0] = v1
    return v0.min()

  # odd <-> even <-> odd
  def min_odd_even_odd():
    a = np.hstack((np.array([-inf]), g, np.array([inf])))
    v0 = np.abs(r - a[np.searchsorted(a, r)])
    v1 = np.abs(r - a[np.searchsorted(a, r, side='right') - 1])
    v0[v1 < v0] = v1

    a = np.hstack((np.array([-inf]), b, np.array([inf])))
    v2 = np.abs(r - a[np.searchsorted(a, r)])
    v3 = np.abs(r - a[np.searchsorted(a, r, side='right') - 1])
    v2[v3 < v2] = v3

    idx0 = np.argsort(v0)
    idx1 = np.argsort(v2)
    if idx0[0] != idx1[1]:
      return v0[idx0[0]] + v2[idx1[0]]


    return min(
      v0[idx0[0]] + v2[idx1[1]],
      v0[idx0[1]] + v2[idx1[0]],
    )

  res = min_odd_odd()
  if len(r) == 0:
    print(res)
    return

  res = min(res, min_odd_even_odd())
  print(res)


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  a, c = np.array(
    sys.stdin.buffer.read().split(),
    dtype='S1',
  ).reshape(2 * n, 2).T
  a = a.astype(np.int64)
  c[c == b'R'] = 0
  c[c == b'G'] = 1
  c[c == b'B'] = 2
  c = c.astype(np.int64)
  solve(a, c)


main()
