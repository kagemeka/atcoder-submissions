import sys
import numpy as np


def is_sorted(
  a: np.array,
) -> bool:
  return np.all(
    np.sort(a) == a,
  )


def solve():
  a = list(map(int, list(input())))
  a.append(10)
  a = a[::-1]
  n = len(a)
  dp = [
    [1] * 4
    for _ in range(n)
  ]
  for i in range(n):
    dp[i][0] = 0
  for i in range(n - 1):
    d0 = a[i]
    d1 = a[i + 1]
    for j in range(1, 4):
      dp[i + 1][j] &= dp[i][j]
      ok = 1 <= d1 <= 3 * j
      dp[i + 1][j] &= ok
      ok = (d1 + 2) // 3 <= d0
      dp[i + 1][j] &= ok
  res = dp[-1]
  for k in range(1, 4):
    if not res[k]: continue
    print(k)
    return
  print(4)



def main():
  t = int(input())
  for _ in range(t):
    solve()


main()
