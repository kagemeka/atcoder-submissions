

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
  print(*dp[1:], sep='\n')



main()
