import sys
import numpy as np
from heapq import heappop, heappush


def main():
    H, W = map(int, sys.stdin.readline().split())

    grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)], dtype='U')
    grid = np.pad(grid, 1, mode='constant')

    can_go = False
    i = j = 1 # start
    c = 0     # real cost
    h = max(H - i, W - j) # goalまでの推定cost
    s = c + h # score
    q = [] # open list
    heappush(q, (s, c, i, j))
    visited = set() # closed list
    # parent = [[None * (W + 1)] for _ in range(H+1)]

    while q:
        s, c, i, j = heappop(q)
        visited.add((i, j))
        if c == s:
            can_go = True
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if grid[y][x] == '.' and not (y, x) in visited:
                visited.add((y, x))
                h = max(H - y, W - x)
                s = h + c + 1
                heappush(q, (s, c+1, y, x))

    if can_go:
        ans = (grid == '.').sum() - (c + 1)
    else:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
