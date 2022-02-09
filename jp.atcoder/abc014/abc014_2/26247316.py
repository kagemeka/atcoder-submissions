import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, x: int) -> typing.NoReturn:
  s = 0
  for i in range(len(a)):
    s += a[i] * (x >> i & 1)
  print(s)

def main() -> typing.NoReturn:
  n, x = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, x)


main()
