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
    p = list(map(lambda x: int(x) - 1, input().split()))

    # g = [[] for _ in range(n)]
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        uf.unite(a, b)


    cnt = 0
    for i in range(n):
        cnt += uf.find(i) == uf.find(p[i])
    print(cnt)

main()
