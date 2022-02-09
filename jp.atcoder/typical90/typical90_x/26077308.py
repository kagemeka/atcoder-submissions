import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:], nb.i8), cache=True)
def solve(
  a: np.ndarray,
  b: np.ndarray,
  k: int,
) -> typing.NoReturn:
  n = len(a)
  d = 0
  for i in range(n):
    d += abs(a[i] - b[i])

  k -= d
  ans = 'Yes' if k >= 0 and k & 1 == 0 else 'No'
  print(ans)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, b, k)


main()
