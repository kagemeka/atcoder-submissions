import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def bit_count(n: int) -> int:
  cnt = 0
  while n:
    cnt += n & 1
    n >>= 1
  return cnt


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
  for s in range(1 << n):
    if bit_count(s) != p: continue
    a = np.zeros(m, np.int64)
    for i in range(n):
      if ~s >> i & 1: continue
      a += g[i]
    mx = max(mx, np.sort(a)[-q:].sum())
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
