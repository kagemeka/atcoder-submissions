import sys
import numpy as np

h, w = map(int, sys.stdin.readline().split())
grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(h)], dtype='U1')
grid = np.pad(grid, 1, 'constant')
grid = grid == '#'

def main():
    res = grid[1:-1, 1:-1]
    l = grid[1:-1, :-2]
    r = grid[1:-1, 2:]
    u = grid[:-2, 1:-1]
    d = grid[2:, 1:-1]
    ans = 'No' if np.any(res & ~(l | r | u | d)) else 'Yes'
    print(ans)

if __name__ ==  '__main__':
    main()
