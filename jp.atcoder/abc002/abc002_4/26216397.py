import typing
import sys
import numpy as np
# import numba as nb


# @nb.njit
def bit_count(n: int) -> int:
  cnt = 0
  while n:
    cnt += n & 1
    n >>= 1
  return cnt


# @nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, xy: np.ndarray) -> typing.NoReturn:
  relation = 1 << np.arange(n)
  m = len(xy)
  for i in range(m):
    x, y = xy[i]
    relation[x] |= 1 << y
    relation[y] |= 1 << x

  mx = 0
  for s in range(1 << n):
    t = s
    for i in range(n):
      if ~s >> i & 1: continue
      t &= relation[i]
    if t == s:
      mx = max(mx, bit_count(s))
  print(mx)



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, xy)


main()
