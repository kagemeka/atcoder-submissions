import typing
import sys
# import numpy as np
# import numba as nb


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n


    def find(self, u: int) -> int:
        if self.__data[u] < 0: return u
        self.__data[u] = self.find(self.__data[u])
        return self.__data[u]

    def unite(self, u: int, v: int) -> typing.NoReturn:
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.__data[u] > self.__data[v]: u, v = v, u
        self.__data[u] += self.__data[v]
        self.__data[v] = u



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    k = 0
    res = [-1] * n
    res[-1] = 0
    uf = UnionFind(n)
    for u in range(n - 1, 0, -1):
        k += 1
        for v in g[u]:
            if v <= u: continue
            if uf.find(v) == uf.find(u): continue
            k -= 1
            uf.unite(u, v)
        res[u - 1] = k
    print(*res)

main()
