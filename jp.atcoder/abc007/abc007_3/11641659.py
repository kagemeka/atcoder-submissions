import sys
from heapq import heappush, heappop
inf = float('inf')

def heuristic_cost(y, x, gy, gx):
    return abs(gy - y) + abs(gx - x)

def a_star(graph, sy, sx, gy, gx):
    h, w = len(graph), len(graph[0])
    dist = [[inf] * w for _ in range(h)]
    parent = [[None] * w for _ in range(h)]
    dyx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(heuristic_cost(sy, sx, gy, gx), 0, sy, sx, None)]
    while q:
        _, d, y, x, p = heappop(q)
        if dist[y][x] != inf: continue
        dist[y][x] = d
        parent[y][x] = p
        if y == gy and x == gx: break
        for dy, dx in dyx:
            i, j = y + dy, x + dx
            if graph[i][j] and dist[i][j] == inf:
                score = heuristic_cost(i, j, gy, gx) + d + 1
                heappush(q, (score, d + 1, i, j, (y, x)))
    return dist, parent

h, w, a, b, c, d, *g = sys.stdin.read().split()
h, w, a, b, c, d = map(int, [h, w, a, b, c, d])
a -= 1; b -= 1; c -= 1; d -= 1

def main():
    graph = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            graph[i][j] = g[i][j] == '.'

    dist, _ = a_star(graph, a, b, c, d)
    print(dist[c][d])

if __name__ == '__main__':
    main()
