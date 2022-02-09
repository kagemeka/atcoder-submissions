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
    # UnionFind
    n, m = map(int, input().split())

    uf = UnionFind(n)
    groups = [[] for _ in range(m)]
    for i in range(n):
        k, *l = map(int, input().split())
        for g in l:
            groups[g - 1].append(i)


    for g in groups:
        k = len(g)
        for i in range(k - 1):
            u, v = g[i], g[i + 1]
            uf.unite(u, v)


    root = [uf.find(i) for i in range(n)]
    print('YES' if len(set(root)) == 1 else 'NO')

main()
