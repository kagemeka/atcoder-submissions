import sys
from heapq import heappop, heappush

import numpy as np

I = np.array(sys.stdin.read().split())
R, C, sy, sx, gy, gx = I[:6].astype(np.int64) - 1
R += 1
C += 1
grid = I[6:]


def heuristicCost(y, x):
    return abs(gy - y) + abs(gx - x)


def main():
    q = []
    h0 = heuristicCost(sy, sx)
    c0 = 0
    s0 = h0 + c0
    heappush(q, (s0, c0, sy, sx))
    visited = np.zeros((R, C), dtype=np.int64)
    parent = [[None] * C for _ in range(R)]
    dist = np.full((R, C), np.inf)
    while q:
        s, d, y, x = heappop(q)
        if visited[y][x]:
            continue
        visited[y][x] = 1
        dist[y][x] = d
        if y == gy and x == gx:
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i = y + dy
            j = x + dx
            if grid[i][j] == "." and not visited[i][j]:
                parent[i][j] = (y, x)
                h = heuristicCost(i, j)
                s = h + d + 1
                heappush(q, (s, d + 1, i, j))

    print(int(dist[y][x]))


if __name__ == "__main__":
    main()

# A*
# 今回は必要ないがdistとparentも一応記録しておく。
