import sys
from heapq import heappush,heappop

inf = float('inf')

n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)

s, t = map(int, sys.stdin.readline().split())

def main():
    dist = [inf] * (n + 1)
    can_reach = [[False] * 3 for _ in range(n + 1)]
    hq = [(0, s)]
    can_reach[s][0] = True
    while hq:
        d, x = heappop(hq)
        if d % 3 == 0:
            dist[x] = min(dist[x], d // 3)
        d += 1
        for y in g[x]:
            if not can_reach[y][d%3]:
                can_reach[y][d%3] = True
                heappush(hq, (d, y))

    return dist[t] if dist[t] != inf else -1

if __name__ == '__main__':
    ans = main()
    print(ans)
