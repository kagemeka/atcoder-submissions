import sys


def main():
  h, w = map(
    int,
    sys.stdin.readline().split(),
  )
  a = [
    [
      1 if x == '+' else -1
      for x in list(
        sys.stdin.readline().rstrip()
      )
    ]
    for _ in range(h)
  ]
  inf = 1 << 30
  dp = [
    [-inf] * w
    for _ in range(h)
  ]
  dp[-1][-1] = 0
  for y in range(h - 1, -1, -1):
    for x in range(w - 1, - 1, -1):
      if y < h - 1:
        dp[y][x] = max(
          dp[y][x],
          dp[y + 1][x] + a[y + 1][x],
        )
      if x < w - 1:
        dp[y][x] = max(
          dp[y][x],
          dp[y][x + 1] + a[y][x + 1],
        )
      dp[y][x] *= -1
  res = dp[0][0]
  print(
    'Takahashi' if res < 0
    else 'Aoki' if res > 0
    else 'Draw'
  )



main()
