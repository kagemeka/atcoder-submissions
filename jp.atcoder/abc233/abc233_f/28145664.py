import typing


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> typing.NoReturn:
        u, v = self.find(u), self.find(v)
        if u == v: return
        d = self.__data
        if d[u] > d[v]: u, v = v, u
        d[u] += d[v]
        d[v] = u



def bfs_sparse(
    g: typing.List[typing.List[int]],
    src: int,
) -> typing.List[int]:
    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    que = [src]
    prev = [None] * n
    for u in que:
        for v, i in g[u]:
            dv = dist[u] + 1
            if dv >= dist[v]: continue
            dist[v] = dv
            prev[v] = (u, i)
            que.append(v)
    return dist, prev



def main() -> typing.NoReturn:
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    m = int(input())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    # K = 5 * 10 ** 5

    # swap target
    # check connectivity with UnionFind
    # O(N^2)
    # do not reswap fixed index
    # lowlink?
    # Articulation Points should be processed at last
    # n - 1 + n - 2 + ... + 1 = n * (n - 1) / 2 <= 5 * 10 ** 5
    # per groups
    # no, process in order of farest point from a certain root.

    g = [[] for _ in range(n)]
    uf = UnionFind(n)
    for i, (a, b) in enumerate(ab):
        g[a].append((b, i))
        g[b].append((a, i))
        uf.unite(a, b)



    for i in range(n):
        if uf.find(i) == uf.find(p[i]): continue
        print(-1)
        return


    inf = 1 << 60
    added = [False] * n

    # que = []
    # for u in range(n):
    #     if added[u]: continue
    #     dist, _ = bfs_sparse(g, u)
    #     cand = [(v, dist[v]) for v in range(n) if dist[v] != inf]
    #     cand.sort(key=lambda x: -x[1])
    #     for v, d in cand:
    #         que.append(v)
    #         added[v] = True

    idx = [-1] * n
    for i in range(n):
        idx[p[i]] = i
    # swap move from idx[i] -> que[i]
    # idx[i] is variable while processing
    # print(que)
    # print(idx)
    # print(p)


    # que = []
    res = []
    for u in range(n):
        if added[u]: continue
        dist, _ = bfs_sparse(g, u)
        cand = [(v, dist[v]) for v in range(n) if dist[v] != inf]
        cand.sort(key=lambda x: -x[1])
        for v, d in cand:
            tgt = v
            added[v] = True
            # que.append(v)
            # added[v] = True
            src = idx[tgt]
            dist, prev = bfs_sparse(g, src)
            order = [tgt]
            edges = []
            assert dist[tgt] != inf
            u = tgt
            while u != src:
                u, e = prev[u]
                order.append(u)
                edges.append(e)
            order = order[::-1]
            edges = edges[::-1]
            for i in range(len(edges)):
                u, v = order[i], order[i + 1]
                e = edges[i]
                res.append(e)
                nu, nv = p[u], p[v]
                p[u], p[v] = p[v], p[u]
                idx[nu] = v
                idx[nv] = u
    # assert len(que) == n

    # res = []
    # for i in range(n):
    #     tgt = que[i]
    #     src = idx[tgt]
    #     dist, prev = bfs_sparse(g, src)
    #     order = [tgt]
    #     edges = []
    #     assert dist[tgt] != inf
    #     u = tgt
    #     while u != src:
    #         u, e = prev[u]
    #         order.append(u)
    #         edges.append(e)
    #     order = order[::-1]
    #     edges = edges[::-1]
    #     for i in range(len(edges)):
    #         u, v = order[i], order[i + 1]
    #         e = edges[i]
    #         res.append(e)
    #         nu, nv = p[u], p[v]
    #         p[u], p[v] = p[v], p[u]
    #         idx[nu] = v
    #         idx[nv] = u
    print(len(res))
    print(*[e + 1 for e in res])






main()
