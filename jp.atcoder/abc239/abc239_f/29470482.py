# from __future__ import annotations

import typing
# import heapq


class UnionFind:
    __data: typing.List[int]

    def __init__(self, size: int) -> None:
        self.__data = [-1] * size

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        self.__data[node] = self.find_root(self.__data[node])
        return self.__data[node]

    def unite(self, node_u: int, node_v: int) -> None:
        assert 0 <= node_u < len(self) and 0 <= node_v < len(self)
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]


def get_labels(uf: UnionFind) -> typing.List[int]:
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        root = uf.find_root(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels


def main() -> None:
    n, m = map(int, input().split())
    d = list(map(int, input().split()))

    g = [[] for _ in range(n)]

    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    deg = [0] * n
    uf = UnionFind(n)

    for a, b in ab:
        g[a].append(b)
        g[b].append(a)
        deg[a] += 1
        deg[b] += 1
        uf.unite(a, b)

    if sum(d) != 2 * (n - 1):
        print(-1)
        return

    # print(d, deg)
    for i in range(n):
        if deg[i] > d[i]:
            print(-1)
            return
        d[i] -= deg[i]

    labels = get_labels(uf)
    # k = len(labels)
    cand = [[] for _ in range(n)]
    deg_sum = [0] * n
    for i in range(n):
        if d[i] > 0:
            cand[uf.find_root(i)].append(i)
            deg_sum[uf.find_root(i)] += d[i]

    roots = list(set(uf.find_root(i) for i in range(n)))
    roots.sort(key=lambda x: deg_sum[x])

    r = len(roots) - 1
    x = roots[r]
    res = []
    while True:
        if r == 0:
            break
        r -= 1
        y = roots[r]
        if len(cand[y]) == 0:
            print(-1)
            return
        while d[cand[x][-1]] == 0:
            cand[x].pop()
        res.append((cand[x][-1], cand[y][-1]))
        d[cand[y][-1]] -= 1
        d[cand[x][-1]] -= 1
        uf.unite(x, y)
        cand[x] += cand[y]
        cand[y].clear()
    for u, v in res:
        print(u + 1, v + 1)


if __name__ == "__main__":
    main()
