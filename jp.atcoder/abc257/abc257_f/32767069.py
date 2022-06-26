# / mypy: ignore-errors
import typing

# T = typing.TypeVar("T")
# E = typing.TypeVar("E")
# G = typing.List[typing.List[E]]
# Q = typing.TypeVar("Q")


# def dijkstra_sparse_general(
#     g: G,
#     data: typing.List[T],
#     que: Q,
# ) -> typing.List[T]:
#     n = len(g)


def main() -> None:
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    inf = 1 << 60

    def bfs(src: int) -> typing.List[int]:
        dist = [inf] * (n + 1)
        dist[src] = 0
        que = [src]
        for u in que:
            for v in g[u]:
                dv = dist[u] + 1
                if dv >= dist[v]:
                    continue
                dist[v] = dv
                que.append(v)
        return dist

    dist_1 = bfs(0)
    dist_n = bfs(n - 1)
    res = [
        min(dist_1[n - 1], dist_1[i] + dist_n[-1], dist_1[-1] + dist_n[i])
        for i in range(n)
    ]
    print(*(-1 if d == inf else d for d in res))


main()
