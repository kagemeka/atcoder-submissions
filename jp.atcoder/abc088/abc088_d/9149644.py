import sys
from heapq import heappop, heappush

H, W = map(int, sys.stdin.readline().split())
grid = ['#' * (W + 2)]
grid += ['#' + sys.stdin.readline().rstrip() + '#' for _ in range(H)]
grid += ['#' * (W + 2)]

def heuristic_cost(y, x):
    return abs(H - y) + abs(W - x)

def main():
    h = heuristic_cost(1, 1)
    c = 0
    s = h + c
    hq = [(s, c, 1, 1)]
    nex = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cost = [[None] * (W+1) for _ in range(H+1)]
    while hq:
        s, c, y, x = heappop(hq)
        if not cost[y][x] is None:
            continue
        cost[y][x] = c
        for dy, dx in nex:
            i = y + dy
            j = x + dx
            if grid[i][j] == '.' and cost[i][j] is None:
                h = heuristic_cost(i, j)
                s = h + (c + 1)
                heappush(hq, (s, c+1, i, j))

    white_cnt = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            white_cnt += (grid[i][j] == '.') & 1

    ans = white_cnt - (cost[H][W] + 1) if not cost[H][W] is None else -1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
