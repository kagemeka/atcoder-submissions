import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i4[:], nb.i4), cache=True)
def solve(a: np.ndarray, k: int) -> typing.NoReturn:
  n = a.size
  for i in range(n):
    a[i] = min(a[i], k)

  def compute_dp(a):
    dp = np.zeros((n + 1, k), np.int16)
    dp[0, 0] = 1
    for i in range(n):
      dp[i + 1] = dp[i].copy()
      for j in range(k - a[i]):
        dp[i + 1, j + a[i]] |= dp[i, j]
    return dp

  dp_l = compute_dp(a)
  dp_r = compute_dp(a[::-1])[::-1]
  for i in range(n + 1):
    for j in range(k - 1):
      dp_r[i, j + 1] += dp_r[i, j]

  def is_needed(i):
    l = dp_l[i]
    r = dp_r[i + 1]
    for x in range(k):
      if not l[x]: continue
      s = r[k - 1 - x]
      if k - a[i] - x > 0:
        s -= r[k - a[i] - x - 1]
      if s >= 1: return True
    return False

  cnt = n
  for i in range(n):
    cnt -= is_needed(i)
  print(cnt)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int32,
  )
  solve(a, k)


main()
