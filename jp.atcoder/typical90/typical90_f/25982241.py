import typing
import sys
import numpy as np
import numba as nb
import heapq



@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(s: np.ndarray, k: int) -> np.ndarray:
  n = s.size
  hq = [(0, 0)] * 0
  for i in range(n - k):
    heapq.heappush(hq, (s[i], i))

  res = np.empty(k, np.int64)
  l = -1
  for i in range(k):
    j = n - k + i
    heapq.heappush(hq, (s[j], j))
    while True:
      x, j = heapq.heappop(hq)
      if j < l: continue
      l = j
      break
    res[i] = x
  return res



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  s = input()
  s = np.array(
    [ord(x) for x in s],
    dtype=np.int64,
  ) - ord('a')
  res = solve(s, k)
  print(''.join([chr(x + ord('a')) for x in res]))



main()
