import typing


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
    n, q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    length = [1] * n
    to_connect = [True] * n  # last state.
    to_connect[0] = False
    for c, x in queries:
        if c == 2:
            continue
        to_connect[x] = False

    uf = UnionFind(n)
    for i in range(n):
        if not to_connect[i]:
            continue
        u, v = uf.find(i - 1), uf.find(i)
        # assert u != v
        sum_len = length[u] + length[v]
        uf.unite(u, v)
        length[uf.find(u)] = sum_len

    res = []
    for c, x in queries[::-1]:
        if c == 1:
            u, v = uf.find(x - 1), uf.find(x)
            # assert u != v
            sum_len = length[u] + length[v]
            uf.unite(u, v)
            length[uf.find(u)] = sum_len
        else:
            res.append(length[uf.find(x)])

    print(*res[::-1], sep='\n')

main()
