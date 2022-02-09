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
    # MST

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    a = sorted(range(n), key=lambda i: xy[i][0])
    b = sorted(range(n), key=lambda i: xy[i][1])

    edges = []
    for i in range(n - 1):
        i, j = a[i], a[i + 1]
        edges.append((i, j, abs(xy[i][0] - xy[j][0])))
    for i in range(n - 1):
        i, j = b[i], b[i + 1]
        edges.append((i, j, abs(xy[i][1] - xy[j][1])))

    edges.sort(key=lambda e: e[2])

    uf = UnionFind(n)
    s = 0
    for u, v, w in edges:
        if uf.find(u) == uf.find(v): continue
        s += w
        uf.unite(u, v)

    print(s)

main()
