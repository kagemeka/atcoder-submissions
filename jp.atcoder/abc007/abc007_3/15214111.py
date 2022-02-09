import sys
import numpy as np

def A():
  n = int(sys.stdin.readline().rstrip())
  print(n-1)


def B():
  s = sys.stdin.readline().rstrip()
  if s == 'a':
    print(-1)
  else:
    print('a')


from collections import deque
def C():
  inf = float('inf')
  r, c = map(int, sys.stdin.readline().split())
  sy, sx = map(int, sys.stdin.readline().split())
  gy, gx = map(int, sys.stdin.readline().split())
  sy -= 1; sx -=1; gy -= 1; gx -= 1
  maze = [sys.stdin.readline().rstrip() for _ in range(r)]
  queue = deque([(sy, sx)])
  dist = np.full((r, c), np.inf); dist[sy, sx] = 0
  while queue:
    y, x = queue.popleft()
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      i += y; j += x
      if maze[i][j] == '#' or dist[i, j] != np.inf:
        continue
      dist[i, j] = dist[y, x] + 1
      queue.append((i, j))
  print(int(dist[gy, gx]))


def D():
  pass


if __name__ == "__main__":
  # A()
  # B()
  C()
  D()
