import sys
from collections import deque

inf = float('inf')

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(sy, sx):
    dist_max = 0
    visited = set()
    queue = deque([(0, sy, sx)])
    while queue:
        d, y, x = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        dist_max = max(dist_max, d)
        for dy, dx in delta:
            i = y + dy
            j = x + dx
            if maze[i][j] == '.' and not (i, j) in visited:
                queue.append((d+1, i, j))
    return dist_max

h, w = map(int, sys.stdin.readline().split())
maze = ['#' * (w + 2)]
maze += ['#' + sys.stdin.readline().rstrip() + '#' for _ in range(h)]
maze += ['#' * (w + 2)]

def main():
    res = 0
    for sy in range(1, h+1):
        for sx in range(1, w+1):
            if maze[sy][sx] == '#':
                continue
            res = max(res, bfs(sy, sx))

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
