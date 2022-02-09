import typing
import sys
sys.setrecursionlimit(1 << 25)
import numpy as np
import numba as nb


@nb.njit
def dfs(
  i: int,
  j: int,
  k: int,
  n: int,
  cache: np.array,
) -> typing.NoReturn:
  if (
    i < 0 or j < 0 or k < 0
  ): return 0
  e = cache[i, j, k]
  if e != -1: return e
  s = i + j + k
  if s == 0: return 0
  e = n
  e += i * dfs(
    i - 1,
    j + 1,
    k,
    n,
    cache,
  )
  e += j * dfs(
    i,
    j - 1,
    k + 1,
    n,
    cache,
  )
  e += k * dfs(
    i,
    j,
    k - 1,
    n,
    cache,
  )
  e /= s
  cache[i, j, k] = e
  return e


@nb.njit(
  (nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  i = (a == 3).sum()
  j = (a == 2).sum()
  k = (a == 1).sum()
  cache = np.full(
    (n + 1, n + 1, n + 1),
    -1,
    dtype=np.float64,
  )
  print(dfs(i, j, k, n, cache))


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
