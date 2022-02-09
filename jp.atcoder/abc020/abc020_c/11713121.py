import sys
import numpy as np
from heapq import heappush, heappop

h, w, t = map(int, sys.stdin.readline().split())
maze = np.array([list(sys.stdin.readline().rstrip()) for _ in range(h)])
maze = np.pad(maze, 1, 'constant')
sy, sx = np.argwhere(maze == 'S')[0]
gy, gx = np.argwhere(maze == 'G')[0]
maze[sy, sx] = maze[gy, gx] = '.'

dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def dijkstra(cost):
    dist = np.full((h + 2, w + 2), np.inf)
    q = [(0, sy, sx)]
    while q:
        d, y, x = heappop(q)
        if dist[y, x] != np.inf: continue
        dist[y, x] = d
        for dy, dx in dyx:
            i = y + dy
            j = x + dx
            if not maze[i, j]: continue
            if dist[i, j] != np.inf: continue
            dd = 1 if maze[i, j] == '.' else cost
            heappush(q, (d + dd, i, j))
    return dist[gy, gx] <= t

def main():
    lo, hi = 1, t
    while lo + 1 < hi:
        x = (lo + hi) // 2
        if dijkstra(x): lo = x
        else: hi = x
    print(lo)

if __name__ ==  '__main__':
    main()
