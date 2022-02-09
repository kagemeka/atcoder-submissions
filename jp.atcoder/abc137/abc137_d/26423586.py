import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def solve(ab: np.ndarray, m: int) -> typing.NoReturn:
  n = len(ab)
  ab = ab[np.argsort(ab[:, 0], kind='mergesort')]
  j = 0
  hq = [0] * 0
  s = 0
  for i in range(1, m + 1):
    while j < n and ab[j, 0] <= i:
      heapq.heappush(hq, -ab[j, 1])
      j += 1
    if not hq: continue
    s += -heapq.heappop(hq)
  print(s)




def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab, m)


main()
