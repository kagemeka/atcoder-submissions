import sys
from collections import deque
inf = float('inf')

def bfs(graph, sy, sx):
    h, w = len(graph), len(graph[0])
    dist = [[inf] * w for _ in range(h)]
    parent = [[None] * w for _ in range(h)]
    dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    q = deque([(0, sy, sx)])
    while q:
        d, y, x = q.popleft()
        if dist[y][x] != inf: continue
        dist[y][x] = d
        for dy, dx in dyx:
            i, j = y + dy, x + dx
            if graph[i][j] and dist[i][j] == inf:
                parent[i][j] = (y, x)
                q.append((d + 1, i, j))
    return dist, parent

h, w, a, b, c, d, *g = sys.stdin.read().split()
h, w, a, b, c, d = map(int, [h, w, a, b, c, d])
a -= 1; b -= 1; c -= 1; d -= 1

def main():
    graph = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            graph[i][j] = g[i][j] == '.'

    dist, _ = bfs(graph, a, b)
    print(dist[c][d])

if __name__ == '__main__':
    main()
