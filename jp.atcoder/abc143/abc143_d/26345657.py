import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(l: np.ndarray) -> typing.NoReturn:
  n = len(l)
  l.sort()
  cnt = 0
  for i in range(n - 2):
    k = 0
    for j in range(i + 1, n - 1):
      while k < n and l[k] < l[i] + l[j]: k += 1
      cnt += k - j - 1
  print(cnt)



def main() -> typing.NoReturn:
  n = int(input())
  l = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(l)


main()
