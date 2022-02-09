import sys
from heapq import heappush, heappop

inf = float('inf')

n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)

s, t = map(int, sys.stdin.readline().split())

g2 = [[] for _ in range(n + 1)]
def after_cand(u):
    hq = [(0, u)]
    visited = set()
    dist = [inf] * (n + 1)
    while hq:
        d, x = heappop(hq)
        if x in visited and d == dist[x]:
            continue
        dist[x] = d
        visited.add(x)
        if d == 3:
            g2[u].append(x)
            continue
        for y in g[x]:
            heappush(hq, (d+1, y))

def main():
    for u in range(1, n+1):
        after_cand(u)

    hq = [(0, s)]
    dist = [inf] * (n + 1)
    while hq:
        d, x = heappop(hq)
        if dist[x] != inf:
            continue
        dist[x] = d
        for y in g2[x]:
            if dist[y] == inf:
                heappush(hq, (d+1, y))

    return dist[t] if dist[t] != inf else -1

if __name__ == '__main__':
    ans = main()
    print(ans)
