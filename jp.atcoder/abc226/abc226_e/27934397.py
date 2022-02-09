import typing


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def __len__(self) -> int: return len(self.__data)

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> bool:
        u, v = self.find(u), self.find(v)
        if u == v: return False
        d = self.__data
        if d[u] > d[v]: u, v = v, u
        d[u] += d[v]
        d[v] = u
        return True

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
    n, m = map(int, input().split())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    uf = UnionFind(n)
    deg = [0] * n
    for u, v in uv:
        uf.unite(u, v)
        deg[u] += 1
        deg[v] += 1

    label = get_labels(uf)
    k = max(label) + 1
    size = [0] * k
    deg_sum = [0] * k
    for i in range(n):
        size[label[i]] += 1
        deg_sum[label[i]] += deg[i]

    MOD = 998_244_353
    p = 1
    for i in range(k):
        p *= (size[i] * 2 == deg_sum[i]) * 2
        p %= MOD
    print(p)

main()
