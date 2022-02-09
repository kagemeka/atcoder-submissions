import typing


def main() -> typing.NoReturn:
  *s, = map(ord, input())
  *t, = map(ord, input())
  n, m = len(s), len(t)

  dp = [
    [0] * (m + 1)
    for _ in range(n + 1)
  ]
  for i in range(n):
    x = s[i]
    for j in range(m):
      dp[i + 1][j + 1] = max(
        dp[i][j + 1],
        dp[i + 1][j],
      )
      if t[j] != x: continue
      dp[i + 1][j + 1] = max(
        dp[i + 1][j + 1],
        dp[i][j] + 1,
      )

  rev = []
  i, j = n - 1, m - 1
  while i >= 0 and j >= 0:
    x = dp[i + 1][j + 1]
    if x > dp[i][j]:
      rev.append(s[i])
      i -= 1
      j -= 1
      continue
    if x == dp[i][j + 1]:
      i -= 1
      continue
    j -= 1
  print(''.join(
    map(chr, reversed(rev)),
  ))



main()
