import sys
import numpy as np
from heapq import heappush, heappop

I = np.array(sys.stdin.read().split())
R, C, sy, sx, gy, gx = I[:6].astype(np.int64) - 1
R += 1
C += 1
grid = I[6:]

def main():
    q = []
    heappush(q, (0, sy, sx))
    visited = np.zeros((R, C), dtype=np.int64)
    parent = [[None] * C for _ in range(R)]
    dist = np.full((R, C), np.inf)
    while q:
        d, y, x = heappop(q)
        if visited[y][x]:
            continue
        visited[y][x] = 1
        dist[y][x] = d
        if y == gy and x == gx:
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i = y + dy
            j = x + dx
            if grid[i][j] == '.' and not visited[i][j]:
                parent[i][j] = (y, x)
                heappush(q, (d + 1, i, j))

    print(int(dist[gy][gx]))

if __name__ == '__main__':
    main()

# Dijkstra
# 今回は必要ないがdistとparentも一応記録しておく。
