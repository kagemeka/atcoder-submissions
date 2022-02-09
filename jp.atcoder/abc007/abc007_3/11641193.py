import sys
from heapq import heappush, heappop
inf = float('inf')

def dijkstra(graph, sy, sx, gy, gx):
    h, w = len(graph), len(graph[0])
    dist = [[inf] * w for _ in range(h)]
    parent = [[None] * w for _ in range(h)]
    q = [(0, sy, sx, None)]
    dyx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        d, y, x, p = heappop(q)
        if dist[y][x] != inf: continue
        dist[y][x] = d
        parent[y][x] = p
        if y == gy and x == gx: break
        for dy, dx in dyx:
            i, j = y + dy, x + dx
            if graph[i][j] and dist[i][j] == inf:
                heappush(q, (d + 1, i, j, (y, x)))
    return dist, parent

h, w, a, b, c, d, *g = sys.stdin.read().split()
h, w, a, b, c, d = map(int, [h, w, a, b, c, d])
a -= 1; b -= 1; c -= 1; d -= 1

def main():
    graph = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            graph[i][j] = g[i][j] == '.'

    dist, _ = dijkstra(graph, a, b, c, d)
    print(dist[c][d])

if __name__ == '__main__':
    main()
