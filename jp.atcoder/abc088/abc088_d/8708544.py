import sys
import numpy as np
from heapq import heappop, heappush

# Dijikstra
def main():
    H, W = map(int, sys.stdin.readline().split())

    grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)])
    grid = np.pad(grid, 1, 'constant')
    # atcoderではnp.pad() のargにconstant_valuesを指定できない
    q = []
    heappush(q, (0, 1, 1))
    visited = set()
    can_go = False
    while q:
        cost, i, j = heappop(q)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == H and j == W:
            can_go = True
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if grid[y][x] == '.' and not (y, x) in visited:
                heappush(q, (cost + 1, y, x))

    if can_go:
        ans = np.sum(grid == '.') - (cost + 1)
    else:
        ans = -1

    print(ans)
if __name__ == "__main__":
    main()
