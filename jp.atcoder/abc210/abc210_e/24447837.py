
import sys
import numpy as np
import typing
import numba as nb


@nb.njit
def gcd(
  a: int,
  b: int,
) -> int:
  if not b:
    return a if a >= 0 else -a
  return gcd(b, a % b)


@nb.njit
def solve(
  n: int,
  a: np.array,
  c: np.array,
) -> typing.NoReturn:
  g = n
  s = 0
  for i in range(a.size):
    g = gcd(g, a[i])
    s += g * c[i]
  print(
    -1 if g != 1 else s,
  )


def main() -> typing:
  n, m = map(
    int,
    input().split(),
  )
  a, c = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2).T
  i = np.argsort(c)
  a, c = a[i], c[i]
  solve(n, a, c)


main()
