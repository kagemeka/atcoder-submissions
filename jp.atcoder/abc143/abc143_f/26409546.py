import typing
import  sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  b = np.zeros(n, np.int64)
  for x in a: b[x - 1] += 1
  b.sort()
  s = np.hstack((np.array([0]), b)).cumsum()

  t = n + 1
  i = n
  for k in range(1, n + 1):
    while not t * (n - i) + s[i] >= t * k:
      while i - 1 >= 0 and not b[i - 1] < t: i -= 1
      t -= 1
    print(t)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
