import sys
inf = float('inf')

n, m = map(int, sys.stdin.readline().split())
graph = [None] * m
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  res = 0
  for c in map(int, sys.stdin.readline().split()):
    res |= 1 << (c - 1)
    graph[i] = (a, res)


def main():
  dp = [[0] * (1 << n) for _ in range(m + 1)]
  for i in range(1, 1 << n):
    dp[0][i] = inf

  for i in range(m):
    for j in range(1 << n):
      dp[i+1][j] = min(dp[i][j ^ (j & graph[i][1])] + graph[i][0], dp[i][j])

  ans = dp[m][(1<<n)-1]
  print(-1 if ans == inf else ans)

if __name__ == '__main__':
  main()
