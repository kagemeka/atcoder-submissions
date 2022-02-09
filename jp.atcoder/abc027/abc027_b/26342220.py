import typing
import sys
import numpy as np
import numba as nb

@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  m = a.sum()
  if m % n:
    print(-1)
    return
  m //= n

  l = 0
  cnt = 0
  s = 0
  for i in range(n):
    s += a[i]
    if (i - l + 1) * m == s:
      cnt += i - l
      s = 0
      l = i + 1
  print(cnt)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
