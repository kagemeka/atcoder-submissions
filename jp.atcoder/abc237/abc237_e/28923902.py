import typing
import heapq

INF = 1 << 60


def dijkstra(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
) -> typing.List[int]:
    n = len(graph)
    dist = [INF] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]:
            continue
        for v, w in graph[u]:
            dv = du + w
            if dv >= dist[v]:
                continue
            dist[v] = dv
            heapq.heappush(hq, (dv, v))
    return dist


def main() -> None:
    # reduce negative edges as possible
    # dijkstra for foucsing on negative happiness edges.
    # positive edges -> 0 cost
    # reverse edge signs.
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if h[u] > h[v]:
            u, v = v, u
        # h[u] < h[v]
        # u -> v: negative edges -> reverse sign.
        # v -> positive edges -> 0 cost.
        graph[u].append((v, (h[v] - h[u])))
        graph[v].append((u, 0))

    # print(graph)
    dist = dijkstra(graph, 0)
    # print(dist)
    res = [h[0] - h[i] + dist[i] - 2 * dist[i] for i in range(n)]
    print(max(res))


if __name__ == "__main__":
    main()
