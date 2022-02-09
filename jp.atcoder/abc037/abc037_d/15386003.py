import sys
MOD=10**9+7

def D():
  h, w = map(int, sys.stdin.readline().split())
  a = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
  dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  b = sorted((a[i][j], i, j) for i in range(h) for j in range(w))
  res = [[1]*w for _ in range(h)]
  for val, i, j in b:
    for dy, dx in dyx:
      y = i+dy; x = j+dx
      if 0<=y<h and 0<=x<w and a[y][x]>val:
        res[y][x] += res[i][j]
        res[y][x] %= MOD
  tot = 0
  for i in range(h):
    tot += sum(res[i])%MOD
    tot %= MOD
  print(tot)

if __name__ == '__main__':
  D()
