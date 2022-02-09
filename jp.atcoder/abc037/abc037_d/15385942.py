import sys
MOD=10**9+7
from functools import lru_cache
sys.setrecursionlimit(10**7)

def D():
  h, w = map(int, sys.stdin.readline().split())
  a = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
  dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

  # path = [[None]*w for _ in range(h)]
  @lru_cache
  def paths(i, j):
    # if path[i][j]: return path[i][j]
    val = a[i][j]
    cnt = 1
    for dy, dx in dyx:
      y = i+dy; x = j+dx
      if 0<=y<h and 0<=x<w and a[y][x]<val:
        cnt += paths(y, x)
        cnt %= MOD
    # path[i][j] = cnt
    return cnt
  tot = 0
  for i in range(h):
    for j in range(w):
      tot += paths(i, j)
      tot %= MOD
  print(tot)

if __name__ == '__main__':
  D()
