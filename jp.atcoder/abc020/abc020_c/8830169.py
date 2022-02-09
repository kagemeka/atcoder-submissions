import sys
from heapq import heappush, heappop
import numpy as np
# 方針: A*, binary-search

H, W, T = map(int, sys.stdin.readline().split())
grid = np.array([list(s) for s in sys.stdin.read().split()])
grid = np.pad(grid, 1, 'constant')
sy, sx = np.argwhere(grid == 'S')[0]
gy, gx = np.argwhere(grid == 'G')[0]
grid[sy, sx] = '.'
grid[gy, gx] = '.'

def heuristic_cost(y, x):
    return abs(gy - y) + abs(gx - x)

heap = []
h0 = heuristic_cost(sy, sx)
c0 = 0
s0 = h0 + c0
heappush(heap, (s0, c0, sy, sx))

def a_star(cost):
    q = heap.copy()
    visited = set()
    while q:
        s, c, y, x = heappop(q)
        if y == gy and x == gx:
            break
        if (y, x) in visited:
            continue
        visited.add((y, x))
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i = y + dy
            j = x + dx
            if not (i, j) in visited:
                h = heuristic_cost(i, j)
                if grid[y, x] == '.':
                    s = h + c + 1
                    heappush(q, (s, c+1, i, j))
                elif grid[y, x] == '#':
                    s = h + c + cost
                    heappush(q, (s, c+cost, i, j))
    return c

def main():
    lo, hi = 1, T
    while lo <= hi:
        m = (lo + hi) // 2
        if a_star(m) > T:
            hi = m - 1
        else:
            lo = m + 1
    return hi

if __name__ == '__main__':
    ans = main()
    print(ans)
