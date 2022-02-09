import typing



def solve(
  g: typing.List[
    typing.List[bool],
  ],
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  h, w = len(g), len(g[0])
  dp = [0] * w
  dp[0] = 1
  for i in range(h):
    for j in range(w - 1):
      dp[j + 1] += (
        dp[j] * g[i][j]
      )
    for j in range(w):
      dp[j] *= g[i][j]
      dp[j] %= mod
  print(dp[-1])


def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  g = [
    [
      x == '.'
      for x in list(input())
    ]
    for _ in range(h)
  ]
  solve(g)


main()
