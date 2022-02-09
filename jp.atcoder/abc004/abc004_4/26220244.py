import typing


def solve(r: int, g: int, b: int) -> typing.NoReturn:
  inf = 1 << 30
  m = k = 1000
  dp = [[inf] * k for _ in range(m)]
  dp[-500][0] = 0
  for i in range(-500, 500):
    for j in range(k):
      dp[i + 1][j] = dp[i][j]
      x = -100 if j <= r else 0 if j <= r + g else 100
      if j > 0:
        dp[i + 1][j] = min(
          dp[i + 1][j],
          dp[i][j - 1] + abs(i - x),
        )
  print(dp[500][r + g + b])


def main() -> typing.NoReturn:
  r, g, b = map(int, input().split())
  solve(r, g, b)


main()
