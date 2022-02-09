import typing


class UnionFind:
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def find_root(self, node: int) -> int:
        if self.__data[node] < 0:
            return node
        self.__data[node] = self.find_root(self.__data[node])
        return self.__data[node]

    def unite(self, node_u: int, node_v: int) -> None:
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u


def main() -> None:
    n, q = map(int, input().split())
    uf = UnionFind(n + 1)
    for _ in range(q):
        l, r = map(int, input().split())
        uf.unite(l - 1, r)
    print("Yes" if uf.find_root(0) == uf.find_root(n) else "No")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
