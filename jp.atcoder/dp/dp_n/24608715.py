import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def dfs(
  l: int,
  r: int,
  s: np.array,
  cache: np.array,
) -> int:
  if r - l == 1: return 0
  v = cache[l, r]
  if v != 0: return v
  v = 1 << 50

  v = 1 << 40
  for m in range(l + 1, r):
    v = min(
      v,
      dfs(l, m, s, cache)
      + dfs(m, r, s, cache),
    )
  v += s[r] - s[l]
  cache[l, r] = v
  return v


@nb.njit(
  (nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  s = np.zeros(n + 1, np.int64)
  s[1:] = a
  s = np.cumsum(s)
  cache = np.zeros(
    (n + 1, n + 1),
    dtype=np.int64,
  )
  print(dfs(0, n, s, cache))




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
