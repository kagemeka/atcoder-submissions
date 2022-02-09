import sys
from heapq import heappush, heappop

inf = float('inf')

n, x, y = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    g[i].append(i+1)
    g[i+1].append(i)
g[x-1].append(y-1)
g[y-1].append(x-1)

def dijkstra(i):
    dist = [inf] * n
    dist[i] = 0
    q = [(0, i)]
    visited = set()

    while q:
        d, x = heappop(q)
        if x in visited:
            continue
        dist[x] = d
        visited.add(x)
        for y in g[x]:
            if y in visited:
                continue
            heappush(q, (d+1, y))
    return dist

def main():
    res = [0] * (n + 1)
    for i in range(n):
        dist = dijkstra(i)
        for d in dist:
            res[d] += 1
    for c in res[1:-1]:
        print(c // 2)

if __name__ == "__main__":
    main()
