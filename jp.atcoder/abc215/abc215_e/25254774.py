import typing


mod = 998244353


def main() -> typing.NoReturn:
  n = int(input())
  a = [ord(x) - ord('A') for x in input()]

  m = 10
  dp = [[0] * m for _ in range(1 << m)]
  for x in a:
    for s in range((1 << m) - 1, -1, -1):
      if ~s >> x & 1: continue
      dp[s][x] += dp[s][x]
      u = s & ~(1 << x)
      for i in range(m):
        if ~u >> i & 1: continue
        dp[s][x] += dp[u][i]
      dp[s][x] %= mod
    dp[1 << x][x] += 1

  ans = sum(
    sum(x) % mod
    for x in dp
  ) % mod
  print(ans)


main()
