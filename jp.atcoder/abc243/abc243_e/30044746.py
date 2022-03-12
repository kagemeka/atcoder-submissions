class UnionFind:
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def find(self, u: int) -> int:
        if self.__data[u] < 0:
            return u
        self.__data[u] = self.find(self.__data[u])
        return self.__data[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u


import typing


def main() -> None:
    ...

    # minimum spanning tree
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b, c))

    edges.sort(key=lambda e: e[2])

    g = [[] for _ in range(n)]

    uf = UnionFind(n)
    for u, v, c in edges:
        if uf.find(u) == uf.find(v):
            continue
        uf.unite(u, v)
        g[u].append((v, c))
        g[v].append((u, c))

    inf = 1 << 60

    def bfs(src: int) -> typing.List[int]:
        dist = [inf] * n
        dist[src] = 0
        q = [src]
        for u in q:
            for v, w in g[u]:
                dv = dist[u] + w
                if dv >= dist[v]:
                    continue
                dist[v] = dv
                q.append(v)
        return dist

    dists = [bfs(i) for i in range(n)]
    # print(dists)
    cnt = n - 1
    for u, v, w in edges:
        cnt += w < dists[u][v]

    print(m - cnt)


if __name__ == "__main__":
    main()
