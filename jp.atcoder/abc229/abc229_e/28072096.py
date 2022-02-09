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
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    uf = UnionFind(n)
    res = [0] * n
    cnt = 0
    for i in range(n - 1, 0, -1):
        cnt += 1
        for j in g[i]:
            if j < i: continue
            if uf.find(i) == uf.find(j): continue
            uf.unite(i, j)
            cnt -= 1
        res[i - 1] = cnt
    print(*res)

main()
