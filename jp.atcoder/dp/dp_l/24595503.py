import typing



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  dp = [
    [0] * (n + 1)
    for _ in range(n + 1)
  ]
  for w in range(1, n + 1):
    for l in range(n - w + 1):
      r = l + w
      x = dp[l + 1][r]
      y = dp[l][r - 1]
      if (n - w) & 1 ^ 1:
        dp[l][r] = max(
          x + a[l],
          y + a[r - 1],
        )
        continue
      dp[l][r] = min(
        x - a[l],
        y - a[r - 1],
      )
  print(dp[0][n])


def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)


main()
