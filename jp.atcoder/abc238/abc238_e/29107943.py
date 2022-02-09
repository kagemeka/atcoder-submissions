import numpy as np
import numba as nb
import sys

try:
    from numba.experimental import jitclass
except ImportError:
    from numba import jitclass


@jitclass(
    [
        ("__data", nb.int64[:]),
    ]
)
class UnionFind:
    def __init__(self, n: int) -> None:
        self.__data = np.full(n, -1, np.int64)

    def find_root(self, node: int) -> int:
        st = []
        while self.__data[node] >= 0:
            st.append(node)
            node = self.__data[node]
        root = node
        for node in st:
            self.__data[node] = root
        return root

    def unite(self, node_u: int, node_v: int) -> None:
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u


@nb.njit((nb.int64, nb.int64[:, :]), cache=True)
def solve(n: int, lr: np.ndarray) -> None:
    uf = UnionFind(n + 1)
    q = len(lr)
    for i in range(q):
        l, r = lr[i]
        uf.unite(l - 1, r)
    print("Yes" if uf.find_root(0) == uf.find_root(n) else "No")


def main() -> None:
    n, q = map(int, input().split())
    lr = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(q, 2)
    solve(n, lr)


main()
