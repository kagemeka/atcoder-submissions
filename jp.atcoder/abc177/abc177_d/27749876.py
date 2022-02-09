import typing

class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]

    def unite(self, u: int, v: int) -> typing.NoReturn:
        u, v = self.find(u), self.find(v)
        if u == v: return
        d = self.__data
        if d[u] > d[v]: u, v = v, u
        d[u] += d[v]
        d[v] = u



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf.unite(a, b)

    print(max(uf.size(i) for i in range(n)))

main()
