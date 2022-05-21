import sys
import heapq


def main() -> None:
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b, c))

    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = edges[i]
        g[a].append((b, c, i))
        g[b].append((a, c, i))

    q = [(0, -1, 0)]  # dist from 0, edge id, vertex id

    inf = 1 << 60
    dist = [inf] * n
    dist[0] = 0
    added = [False] * m
    while q:
        du, eid, u = heapq.heappop(q)
        if du > dist[u]:
            continue
        if eid >= 0:
            added[eid] = True
        for v, d, eid in g[u]:
            if added[eid]:
                continue
            dv = dist[u] + d
            if dv >= dist[v]:
                continue
            dist[v] = dv
            heapq.heappush(q, (dv, eid, v))
    assert sum(added) == n - 1
    res = [i + 1 for i in range(m) if added[i]]
    print(*res)


if __name__ == "__main__":
    main()
