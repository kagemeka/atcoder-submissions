import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, k: int) -> typing.NoReturn:
  n = a.size
  a.sort()

  def is_needed(i):
    dp = np.zeros(k, np.bool8)
    dp[0] = True
    for j in range(n):
      if j == i: continue
      for l in range(k - a[j] - 1, -1, -1):
        dp[l + a[j]] |= dp[l]
    return np.any(dp[k - a[i]:])

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
