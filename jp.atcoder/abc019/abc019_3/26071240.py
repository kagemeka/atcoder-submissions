import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  b = np.zeros(1 << 20, np.bool8)
  for i in range(n):
    x = a[i]
    while x % 2 == 0: x //= 2
    b[x] = True

  cnt = 0
  for x in b:
    cnt += x
  print(cnt)

def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
