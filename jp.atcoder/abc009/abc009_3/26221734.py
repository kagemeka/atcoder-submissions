import typing
import heapq
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(s: np.ndarray, k: int) -> typing.NoReturn:
  n = len(s)
  swap_cost = np.full(n, 1, np.int64)
  for i in range(n - 1):
    hq = [(0, 0, 0)] * 0
    for j in range(i + 1, n):
      if s[j] >= s[i]: continue
      c = swap_cost[i] + swap_cost[j]
      if c > k: continue
      heapq.heappush(hq, (s[j], c, -j))
    if not hq: continue
    x, c, j = heapq.heappop(hq)
    j = -j
    k -= c
    swap_cost[i] = swap_cost[j] = 0
    s[i], s[j] = s[j], s[i]
  return s


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  *s, = map(ord, input())
  s = np.array(s)
  s = solve(s, k).tolist()
  s = ''.join(chr(x) for x in s)
  print(s)


main()
