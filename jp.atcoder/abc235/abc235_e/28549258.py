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
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b, c, 1, -1))
    for i in range(q):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w, 2, i))
    edges.sort(key=lambda e: e[2])
    res = ['Yes'] * q
    # simulate

    uf = UnionFind(n)
    for u, v, w, t, i in edges:
        if uf.find(u) == uf.find(v) and t == 2:
            res[i] = 'No'
        if t == 2:
            continue
        uf.unite(u, v)

    print(*res, sep='\n')





main()
