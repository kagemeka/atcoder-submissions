import sys
from heapq import heappush, heappop

INF = 10 ** 7

n, m = map(int, sys.stdin.readline().split())
abc = map(int, sys.stdin.read().split())
abc = zip(*[abc] * 3)
graph = [[] for _ in range(n)]
for a, b, c in abc:
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

def dijkstra(v):
    used_edges = [set() for _ in range(n)]
    hq = []
    heappush(hq, (0, v, None))
    dist = [INF] * n
    pars = [set() for _ in range(n)]
    while hq:
        d, x, z = heappop(hq)
        if 0 < dist[x] < INF:
            if d == dist[x]:
                pars[x].add(z)
                used_edges[x] |= used_edges[z]
                if z < x:
                    used_edges[x].add((z, x))
                else:
                    used_edges[x].add((x, z))
            continue

        dist[x] = d
        if x != v:
            used_edges[x] |= used_edges[z]
            pars[x].add(z)
            if z < x:
                used_edges[x].add((z, x))
            else:
                used_edges[x].add((x, z))

        for (y, c) in graph[x]:
            if y in pars[x] or pars[y]:
                continue
            heappush(hq, (d+c, y, x))

    res = set()
    for i in range(n):
        res |= used_edges[i]
    return res

def main():
    res = set()
    for v in range(n):
        res |= dijkstra(v)

    ans = m - len(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
