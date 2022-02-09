import typing


def dijkstra_sparse(
    g: typing.List[typing.Tuple[int, int]],
    src: int,
) -> typing.List[int]:
    import heapq
    n = len(g)
    dist = [None] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]: continue
        for v, w in g[u]:
            dv = du + w
            if dist[v] is not None and dv >= dist[v]: continue
            dist[v] = dv
            heapq.heappush(hq, (dv, v))
    return dist


def main() -> typing.NoReturn:
    n, m, s, t = map(int, input().split())
    s -= 1
    t -= 1
    g1 = [[] for _ in range(n)]
    g2 = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        g1[u].append((v, a))
        g1[v].append((u, a))
        g2[u].append((v, b))
        g2[v].append((u, b))


    cost1 = dijkstra_sparse(g1, s)
    cost2 = dijkstra_sparse(g2, t)

    K = 10 ** 15

    cost = [cost1[i] + cost2[i] for i in range(n)]
    for i in range(n - 1, 0, -1):
        cost[i - 1] = min(cost[i - 1], cost[i])

    for i in range(n):
        print(K - cost[i])

main()
