import sys
import numpy as np

h, w = map(int, sys.stdin.readline().split())
grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(h)], dtype='U1')
grid = np.pad(grid, 1, 'constant')

def main():
  d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  cnt = np.zeros_like(grid, dtype=np.int8)
  for i in range(1, h + 1):
    for j in range(1, w + 1):
      if grid[i][j] == '.': continue
      for dy, dx in [(dy, dx) for dy in range(-1, 2) for dx in range(-1, 2)]:
        cnt[i+dy][j+dx] += 1
  cnt = cnt.astype('U1')
  cnt[grid == '#'] = '#'
  cnt = cnt[1:-1, 1:-1]
  for i in range(h):
    print(''.join(cnt[i]))

if __name__ == '__main__':
  main()
