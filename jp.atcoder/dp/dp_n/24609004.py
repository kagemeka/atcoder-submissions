import typing


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  dp = [
    [0] * (n + 1)
    for _ in range(n + 1)
  ]
  s = [0] * (n + 1)
  s[1:] = a
  for i in range(n):
    s[i + 1] += s[i]

  for w in range(2, n + 1):
    for l in range(n - w + 1):
      r = l + w
      dp[l][r] = min(
        dp[l][m] + dp[m][r]
        for m in range(
          l + 1, r,
        )
      ) + s[r] - s[l]
  print(dp[0][n])



def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(
    int, input().split(),
  )
  solve(n, a)


main()
