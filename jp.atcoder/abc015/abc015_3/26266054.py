import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(t: np.ndarray) -> typing.NoReturn:
  n, k = t.shape
  a = np.zeros(1, np.int64)
  for i in range(n):
    b = []
    for x in a:
      for y in t[i]:
        b.append(x ^ y)
    a = np.unique(np.array(b))
  ans = 'Found' if a[0] == 0 else 'Nothing'
  print(ans)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  t = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, k)
  solve(t)


main()
