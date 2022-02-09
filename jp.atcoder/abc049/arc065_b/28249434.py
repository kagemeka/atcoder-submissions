import typing
import collections

class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def __len__(self) -> int: return len(self.__data)

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

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]


def get_labels(uf: UnionFind) -> typing.List[int]:
    n = len(uf)
    label = [-1] * n
    l = 0
    for i in range(n):
        root = uf.find(i)
        if label[root] == -1:
            label[root] = l
            l += 1
        label[i] = label[root]
    return label


def main() -> typing.NoReturn:
    # UnionFind
    ...
    n, k, l = map(int, input().split())
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf1.unite(a, b)

    for _ in range(l):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf2.unite(a, b)

    label1 = get_labels(uf1)
    label2 = get_labels(uf2)


    cnt = collections.Counter()
    for i in range(n):
        cnt[(label1[i], label2[i])] += 1

    res = []
    res = [cnt[(label1[i], label2[i])] for i in range(n)]
    print(*res)

main()
