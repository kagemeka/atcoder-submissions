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


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, ab: np.ndarray) -> typing.NoReturn:
  m = len(ab)
  g = 1 << np.arange(n)
  for i in range(m):
    a, b = ab[i]
    g[a] |= 1 << b
    g[b] |= 1 << a

  for i in range(n):
    s = 0
    for j in range(n):
      if ~g[i] >> j & 1: continue
      s |= g[j]
    s &= ~g[i]
    print(bit_count(s))

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, ab)


main()
