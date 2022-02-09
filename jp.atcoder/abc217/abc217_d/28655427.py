import typing
import bisect


class UnionFind():
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0:
            return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u


def main() -> None:
    l_max, q = map(int, input().split())
    # n <= 10 ^ 9
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    a = [x for c, x in queries if c == 1] + [l_max]
    n = len(a)
    a.sort()
    length = a.copy()
    for i in range(n - 1, 0, -1):
        length[i] -= length[i - 1]

    uf = UnionFind(n)

    res = []
    for c, x in queries[::-1]:
        i = bisect.bisect_right(a, x)
        if c == 1:
            u, v = uf.find(i - 1), uf.find(i)
            assert u != v
            sum_len = length[u] + length[v]
            uf.unite(u, v)
            length[uf.find(u)] = sum_len
        else:
            res.append(length[uf.find(i)])

    print(*res[::-1], sep='\n')

main()
