import typing
import numpy as np
import sys
import numba as nb



@nb.njit
def solve(
  a: np.array,
  b: np.array,
) -> typing.NoReturn:
  cand = np.unique(a[0] ^ b)
  cand.sort()
  res = []
  b.sort()
  for x in cand:
    y = x ^ a
    y.sort()
    if (y == b).all():
      res.append(x)
  return res


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n)
  x = solve(a, b)
  n = len(x)
  print(n)
  if n: print(*x, sep='\n')


main()
