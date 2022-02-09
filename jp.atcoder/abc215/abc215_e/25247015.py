import typing


mod = 998244353

def main() -> typing.NoReturn:
  n = int(input())
  s = input()
  s = [ord(x) - ord('B') for x in s]
  m = 10

  dp = [[0] * m for _ in range(1 << m)]

  for x in s:
    ndp = [[0] * m for _ in range(1 << m)]
    for u in range(1 << m):
      for i in range(m):
        ndp[u][i] += dp[u][i] * (1 + (i == x))
        ndp[u][i] %= mod

    for u in range(1 << m):
      if u >> x & 1: continue
      v = u | 1 << x
      for i in range(m):
        if ~u >> i & 1: continue
        ndp[v][x] += dp[u][i]
      ndp[v][x] %= mod

    ndp[1 << x][x] += 1
    dp = ndp

  print(sum((sum(x) for x in dp)) % mod)


main()
