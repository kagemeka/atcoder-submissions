import sys
MOD=10**9+7

def D():
  h, w, *a = map(int, sys.stdin.read().split())
  *a, = zip(*[iter(a)]*w)
  queue = []
  for i in range(h):
    for j in range(w):
      queue.append((a[i][j], i, j))
  queue.sort()
  res = [[1]*w for _ in range(h)]
  for val, i, j in queue:
    for y, x in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
      if 0<=y<h and 0<=x<w and a[y][x]>val:
        res[y][x] = (res[y][x]+res[i][j])%MOD
  ans = 0
  for i in range(h):
    ans = (ans+sum(res[i])%MOD)%MOD
  print(ans)

if __name__ == '__main__':
  D()
