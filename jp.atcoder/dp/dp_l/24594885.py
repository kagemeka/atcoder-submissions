import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def dfs(
  l: int,
  r: int,
  a: np.array,
  cache: np.array,
) -> int:
  if l + r == a.size: return 0
  v = cache[l, r]
  if v != 1 << 50: return v
  x = dfs(l + 1, r, a, cache)
  y = dfs(l, r + 1, a, cache)
  if (l + r) & 1 == 0:
    v = max(
      x + a[l],
      y + a[-1 - r],
    )
  else:
    v = min(
      x - a[l],
      y - a[-1 - r],
    )
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
  inf = 1 << 50
  cache = np.full(
    (n + 1, n + 1),
    inf,
    np.int64,
  )
  print(dfs(0, 0, a, cache))



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
