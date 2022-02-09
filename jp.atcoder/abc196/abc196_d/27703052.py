import typing


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n


    def find(self, u: int) -> typing.NoReturn:
        if self.__data[u] < 0: return u
        self.__data[u] = self.find(self.__data[u])
        return self.__data[u]


    def unite(self, u: int, v: int) -> typing.NoReturn:
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.__data[u] > self.__data[v]: u, v = v, u
        self.__data[u] += self.__data[u]
        self.__data[v] = u



import itertools
import collections

def main() -> typing.NoReturn:
    h, w, a, b = map(int, input().split())
    # wall cnt := h * (w - 1) + w * (h - 1)
    edges = []
    for i in range(h * (w - 1)):
        y, x = divmod(i, w - 1)
        i = y * w + x
        edges.append((i, i + 1))

    for i in range(w * (h - 1)):
        edges.append((i, i + w))
    m = len(edges)
    n = h * w

    def is_ok(s: typing.Iterator[int]) -> bool:
        uf = UnionFind(n)
        for i in s:
            u, v = edges[i]
            uf.unite(u, v)
        root = [uf.find(i) for i in range(n)]
        cnt = collections.Counter(root)
        if len(cnt) != a + b: return False
        for u, c in cnt.items():
            if c >= 3: return False
        return True

    cnt = 0
    for s in itertools.combinations(range(m), a):
        cnt += is_ok(s)
    print(cnt)



main()
