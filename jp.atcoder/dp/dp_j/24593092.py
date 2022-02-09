import typing
from collections import (
  Counter,
)


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  dp = [
    [
      [-1] * (n + 1)
      for _ in range(n + 1)
    ]
    for _ in range(n + 1)
  ]
  dp[0][0][0] = 0
  for i in range(n + 1):
    for j in range(n + 1):
      for k in range(n + 1):
        if i + j + k > n:
          continue
        s = i + j + k
        if s == 0: continue
        e = n
        if i > 0:
          e += i * dp[i - 1][j - 1][k]
        if j > 0:
          e += j * dp[i][j - 1][k + 1]
        if k > 0:
          e += k * dp[i][j][k - 1]
        dp[i][j][k] = e / s

  c = Counter(a)
  print(dp[c[3]][c[2]][c[1]])



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)



main()
