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

    g = [[] for _ in range(n)]
    has_tel = [False] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u == -1:
            has_tel[v] = True
        else:
            g[u].append(v)
            g[v].append(u)

    inf = 1 << 60

    def bfs(src: int) -> typing.List[int]:
        dist = [inf] * n
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

    t_1 = inf
    t_n = inf
    for i in range(n):
        if not has_tel[i]:
            continue
        t_1 = min(t_1, dist_1[i])
        t_n = min(t_n, dist_n[i])

    # print(dist_1, dist_n, t_1, t_n)
    res = [dist_1[n - 1]] * n
    for i in range(n):
        d = min(t_1 + 1, dist_1[i]) + min(t_n + 1, dist_n[i])
        res[i] = min(res[i], d)
    print(*(-1 if d == inf else d for d in res))


main()
