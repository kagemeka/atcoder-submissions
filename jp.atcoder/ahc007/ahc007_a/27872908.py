import typing


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]

    def unite(self, u: int, v: int) -> bool:
        u, v = self.find(u), self.find(v)
        if u == v: return False
        d = self.__data
        if d[u] > d[v]: u, v = v, u
        d[u] += d[v]
        d[v] = u
        return True


import itertools
import math
import random
random.seed = 0

def main() -> typing.NoReturn:
    N = 400
    M = 1995

    R = 2
    xy = [tuple(map(int, input().split())) for _ in range(N)]
    inf = 1 << 60
    dist = [[inf] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            xi, yi = xy[i]
            xj, yj = xy[j]
            d = int(round(math.sqrt((xj - xi) ** 2 + (yj - yi) ** 2)))
            r = random.randint(1, 3)
            d *= r
            dist[i][j] = dist[j][i] = d

    uv = [tuple(map(int, input().split())) for _ in range(M)]

    # dist_edge = [dist[uv[i][0]][uv[i][1]]]
    edge_idx = sorted(range(M), key=lambda i: dist[uv[i][0]][uv[i][1]])
    # edge_idx[i] =
    # edges = [(i, j) for i in range(N - 1) for j in range(i + 1, N)]
    # edges.sort(key=lambda uv: dist[uv[0]][uv[1]])
    uf = UnionFind(N)
    to_use = set()
    for i in edge_idx:
        u, v = uv[i]
        if not uf.unite(u, v):
            continue
        to_use.add(i)

    for i in range(M):
        d = int(input())
        print(1 if i in to_use else 0, flush=True)


main()
