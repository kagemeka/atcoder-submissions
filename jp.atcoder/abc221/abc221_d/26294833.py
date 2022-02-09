import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
  n = len(ab)
  a, b = ab[:, 0], ab[:, 1]
  for i in range(n):
    b[i] += a[i]
  c = np.unique(np.hstack((a, b)))
  a = np.searchsorted(c, a)
  b = np.searchsorted(c, b)
  s = np.zeros(1 << 19, np.int64)
  for i in range(n):
    s[a[i]] += 1
    s[b[i]] -= 1
  s = s.cumsum()


  res = np.zeros(n + 1, np.int64)
  for i in range(1 << 19):
    x = s[i]
    if not x: continue
    l, r = c[i], c[i + 1]
    res[x] += r - l

  for x in res[1:]:
    print(x)



def main() -> typing.NoReturn:
  n = int(input())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab)


main()
