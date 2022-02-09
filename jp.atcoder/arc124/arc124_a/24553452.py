import typing
import numpy as np
import sys
import numba as nb


@nb.njit
def solve(
  n: int,
  k: int,
  c: int,
  a: int,
) -> typing.NoReturn:
  mod = 998244353

  b = np.zeros(
    n + 1,
    dtype=np.int64,
  )
  for i in range(k):
    x = a[i]
    if c[i] == 0:
      b[0] -= 1
      b[x] += 1
    else:
      b[x + 1] -= 1
      b[-1] += 1
  for i in range(n):
    b[i + 1] += b[i]
    b[i] += k
  for x in a:
    b[x] = 1
  p = 1
  for x in b[:-1]:
    p *= x
    p %= mod
  print(p)


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  c, a = np.array(
    sys.stdin.read().split(),
  ).reshape(k, 2).T
  a = a.astype(np.int64) - 1
  c = np.where(c == 'L', 0, 1)
  solve(n, k, c, a)


main()
