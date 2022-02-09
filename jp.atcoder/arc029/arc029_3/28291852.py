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


def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    # UnionFind, similar to kruskal

    c = [int(input()) for _ in range(n)]

    abr = [tuple(map(int, input().split())) for _ in range(m)]

    s = sum(c)
    uf = UnionFind(n)
    abr.sort(key=lambda x: x[2])
    for a, b, r in abr:
        a -= 1
        b -= 1
        a = uf.find(a)
        b = uf.find(b)
        if a == b: continue
        if c[a] > c[b]:
            a, b = b, a
        if c[b] < r: continue
        s += r - c[b]
        c[b] = c[a]
        uf.unite(a, b)
    print(s)

main()
