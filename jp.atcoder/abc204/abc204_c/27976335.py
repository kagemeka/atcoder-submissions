import typing


def bfs_sparse(g: typing.List[typing.List[int]], src: int) -> typing.List[int]:
    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    que = [src]
    for u in que:
        for v in g[u]:
            dv = dist[u] + 1
            if dv >= dist[v]: continue
            dist[v] = dv
            que.append(v)
    return dist


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)

    inf = 1 << 60
    cnt = 0
    for i in range(n):
        dist = bfs_sparse(g, i)
        cnt += sum(d != inf for d in dist)
    print(cnt)

main()
