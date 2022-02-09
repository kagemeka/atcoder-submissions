import sys
import numpy as np
from heapq import heappop, heappush

# Dijikstra
def main():
    H, W = map(int, sys.stdin.readline().split())

    grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)])
    grid = np.pad(grid, 1)
    # atcoderではnp.pad() のargにconstant_valuesを指定できない
    q = []
    heappush(q, (0, 1, 1))
    visited = set()
    cost = np.full((H + 1, W + 1), np.inf)
    cost[1][1] = 0
    while q:
        c, i, j = heappop(q)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        cost[i][j] = c
        if i == H and j == W:
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if grid[y][x] == '.' and not (y, x) in visited:
                heappush(q, (c + 1, y, x))


    if cost[H][W] != np.inf:
        ans = int(np.sum(grid == '.') - (cost[H][W] + 1))
    else:
        ans = -1

    print(ans)
if __name__ == "__main__":
    main()
