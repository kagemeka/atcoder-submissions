import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def next_combination(s: int) -> int:
  i = s & -s
  j = s + i
  return (s & ~j) // i >> 1 | j


@nb.njit((nb.i8, ) * 4 + (nb.i8[:, :], ), cache=True)
def solve(
  n: int,
  m: int,
  p: int,
  q: int,
  xyz: np.ndarray,
) -> typing.NoReturn:
  g = np.zeros((n, m), np.int64)
  r = len(xyz)
  for i in range(r):
    x, y, z = xyz[i]
    g[x, y] = z

  mx = 0
  s = (1 << p) - 1
  while s < 1 << n:
    a = np.zeros(m, np.int64)
    for i in range(n):
      if ~s >> i & 1: continue
      a += g[i]
    mx = max(mx, np.sort(a)[-q:].sum())
    s = next_combination(s)
  print(mx)


def main() -> typing.NoReturn:
  n, m, p, q, r = map(int, input().split())
  xyz = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(r, 3)
  xyz[:, :2] -= 1
  solve(n, m, p, q, xyz)


main()
