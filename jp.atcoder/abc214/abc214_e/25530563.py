import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  l: np.ndarray,
  r: np.ndarray,
) -> typing.NoReturn:
  n = l.size
  idx = np.argsort(l)
  l = l[idx]
  r = r[idx]

  h = [0]
  h.pop()
  i, j = 0, 1
  for _ in range(n):
    if not h and i < n: j = l[i]
    while i < n and l[i] == j:
      heapq.heappush(h, r[i])
      i += 1
    if heapq.heappop(h) < j:
      print('No')
      return
    j += 1
  print('Yes')


def main() -> typing.NoReturn:
  t = int(input())

  for _ in range(t):
    n = int(input())
    lr = [
      [int(x) for x in sys.stdin.readline().split()]
      for _ in range(n)
    ]
    l, r = np.array(lr).T
    solve(l, r)


main()
