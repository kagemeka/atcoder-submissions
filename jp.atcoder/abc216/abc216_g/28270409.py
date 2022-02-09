import typing


def dijkstra_sparse(
    g: typing.List[typing.List[int]],
    src: int,
) -> typing.List[typing.Optional[int]]:
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
    n, m = map(int, input().split())
    # m <= min(2 * 10^5, n(n + 1)/n) -> graph problem ?
    # ushi-game ?
    # s[r] - s[l - 1] >= x
    # s[r] - s[l - 1] <= (r - l + 1 - x) (swap 0,1 and maximize the count of 0)
    # there are some constrains such that dist[v] - dist[u] <= x
    # src node is 0.
    # this graph might be unconnected
    # dist[i] <= dist[i + 1] <= dist[i] + 1



    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        l, r, x = map(int, input().split())
        l -= 1
        r -= 1
        g[l].append((r + 1, r + 1 - l - x))

    for i in range(n):
        g[i].append((i + 1, 1))
        g[i + 1].append((i, 0))

    dist = dijkstra_sparse(g, 0)

    res = [0] * n
    for i in range(n):
        if dist[i] == dist[i + 1]: res[i] = 1
    print(*res)

main()
