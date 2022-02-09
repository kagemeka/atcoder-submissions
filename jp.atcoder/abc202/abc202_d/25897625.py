import typing
import sys
import numpy as np
import numba as nb




@nb.njit((nb.i8, nb.i8, nb.i8), cache=True)
def solve(a: int, b: int, k: int) -> typing.NoReturn:

  dp = np.zeros((a + 1, b + 1), np.int64)
  dp[0] = 1
  dp[:, 0] = 1
  for i in range(a):
    for j in range(b):
      dp[i + 1, j + 1] = dp[i + 1, j] + dp[i, j + 1]


  res = np.empty(a + b, np.int64)
  i = 0
  while k:
    if dp[a, b] == k:
      res[i:i + b] = 1
      res[i + b:] = 0
      break
    if k > dp[a - 1, b]:
      k -= dp[a - 1, b]
      b -= 1
      res[i] = 1
    else:
      a -= 1
      res[i] = 0
    i += 1
  return res


def main() -> typing.NoReturn:
  a, b, k = map(int, input().split())
  res = solve(a, b, k)
  print(''.join(map(chr, res + ord('a'))))


main()
