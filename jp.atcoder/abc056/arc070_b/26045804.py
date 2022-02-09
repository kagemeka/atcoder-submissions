import typing
import sys
import numpy as np
import numba as nb



def solve(a: np.ndarray, k: int) -> typing.NoReturn:
  n = a.size
  a.sort()
  np.minimum(a, k, out=a)

  def is_needed(i):
    dp = np.zeros(k * 2, np.bool8)
    dp[0] = True
    for j in range(n):
      if j == i: continue
      l = np.arange(k)
      dp[l + a[j]] |= dp[l]
    return np.any(dp[k - a[i]:k])

  def binary_search():
    lo, hi = -1, n
    while hi - lo > 1:
      i = (lo + hi) // 2
      if is_needed(i):
        hi = i
      else:
        lo = i
    return hi

  print(binary_search())




def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
