import typing


def dijkstra_sparse(
    g: typing.List[int],
    src: int,
) -> typing.List[int]:
    import heapq
    inf = 1 << 60
    n = len(g)
    dist = [inf] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]: continue
        for v, w in g[u]:
            dv = du + w
            if dv >= dist[v]: continue
            dist[v] = dv
            heapq.heappush(hq, (dv, v))
    return dist


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    # bidirectional graph
    # dijkstra from s and t.
    # there exist at least 1 node i such that dist_s[i] = dist_t[i]

    s, t = map(lambda x: int(x) - 1, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        x -= 1
        y -= 1
        g[x].append((y, d))
        g[y].append((x, d))

    inf = 1 << 60
    dist_s = dijkstra_sparse(g, s)
    dist_t = dijkstra_sparse(g, t)
    for i in range(n):
        if dist_s[i] == inf: continue
        if dist_s[i] != dist_t[i]: continue
        print(i + 1)
        return
    print(-1)

main()
