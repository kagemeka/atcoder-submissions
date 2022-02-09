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
    parents = [set() for _ in range(n)]
    while hq:
        d, cur, prev = heappop(hq)
        if dist[cur] != INF:
            if d == dist[cur]:
                parents[cur].add(prev)
                used_edges[cur] |= used_edges[prev]
                if prev < cur:
                    used_edges[cur].add((prev, cur))
                else:
                    used_edges[cur].add((cur, prev))
            continue

        dist[cur] = d
        if cur != v:
            used_edges[cur] |= used_edges[prev]
            parents[cur].add(prev)
            if prev < cur:
                used_edges[cur].add((prev, cur))
            else:
                used_edges[cur].add((cur, prev))

        for (u, c) in graph[cur]:
            if u in parents[cur] or parents[u]:
                continue
            nex = u
            heappush(hq, (d+c, nex, cur))

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
