

def main():
  n = int(input())
  *s, = map(int, input().split())
  *t, = map(int, input().split())


  inf = 1 << 60
  s = [inf] + s
  dp = [inf] * (n + 1)
  for i in range(n):
    dp[i + 1] = min(
      dp[i] + s[i],
      t[i],
    )
  dp[1] = min(dp[-1] + s[-1], dp[1])
  print(*dp[1:], sep='\n')



main()
