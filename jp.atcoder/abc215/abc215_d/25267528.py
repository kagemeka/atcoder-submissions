import typing
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def solve(
  a: np.array,
  m: int,
) -> typing.NoReturn:
  n = a.size
  k = 1 << 20
  s = np.ones(k, dtype=np.bool8)
  s[a] = False

  a = np.ones(m + 1, dtype=np.bool8)
  a[0] = False
  for i in range(2, m + 1):
    if not s[i::i].all(): a[i::i] = False

  print(a.sum())
  for x in np.flatnonzero(a):
    print(x)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, m)


main()
