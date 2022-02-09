import typing


class UnionFind:
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def __len__(self) -> int:
        return len(self.__data)

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0:
            return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]


def main() -> None:
    n, m, q = map(int, input().split())
    abc = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        abc.append((a, b, c))
    # for each node, memolize max weighted edge in advance.
    abc.sort(key=lambda e: e[2])

    uf = UnionFind(n)
    inf = 1 << 30
    max_weight = [inf] * n
    for a, b, c in abc:
        if uf.find(a) == uf.find(b):
            continue
        uf.unite(a, b)
        max_weight[a] = min(max_weight[a], c)
        max_weight[b] = min(max_weight[b], c)

    res = []
    for _ in range(q):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if u == v:
            res.append('No')
            continue
        if max_weight[u] > w or max_weight[v] > w:
            res.append('Yes')
        else:
            res.append('No')

    print(*res, sep='\n')





main()
