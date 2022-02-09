import typing


def main() -> typing.NoReturn:
  *s, = map(ord, input())
  *t, = map(ord, input())
  n, m = len(s), len(t)


  dp = [
    [(0, -1, -1)] * (m + 1)
    for _ in range(n + 1)
  ]
  for i in range(n):
    x = s[i]
    for j in range(m):
      if t[j] == x:
        dp[i + 1][j + 1] = (
          dp[i][j][0] + 1,
          i,
          j,
        )
        continue
      y = dp[i][j + 1][0]
      z = dp[i + 1][j][0]
      dp[i + 1][j + 1] = (
        (y, i, j) if y >= z
        else (z, i, j)
      )

  rev = []
  u = dp[-1][-1]
  while True:
    c, y, x = u
    if y == -1: break
    v = dp[y][x]
    if v[0] < c:
      rev.append(s[y])
    u = v

  res = ''.join(
    map(chr, reversed(rev)),
  )
  print(res)


main()
