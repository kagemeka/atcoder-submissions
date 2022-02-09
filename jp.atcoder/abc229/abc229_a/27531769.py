import typing



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

import itertools

def main() -> typing.NoReturn:
    a = [[x == '#' for x in input()] for _ in range(2)]
    black = []
    for i in range(2):
        for j in range(2):
            if a[i][j]: black.append((i, j))
    uf = UnionFind(4)
    ok = True
    for (yi, xi), (yj, xj) in itertools.combinations(black, 2):
        if yi == yj or xi == xj: uf.unite((yi * 2 + xi), yj * 2 + xj)
    for (yi, xi), (yj, xj) in itertools.combinations(black, 2):
        if uf.find((yi * 2 + xi)) != uf.find(yj * 2 + xj):
            ok = False
    print('Yes' if ok else 'No')
    # ok = True
    # if a[0][1] and a[1][1]:

main()
