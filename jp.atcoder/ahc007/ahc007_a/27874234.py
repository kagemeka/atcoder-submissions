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
# random.seed = 0

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
            # r = sum(random.randint(1, 3) for _ in range(5)) / 5
            d *= R
            dist[i][j] = dist[j][i] = d

    uv = [tuple(map(int, input().split())) for _ in range(M)]

    dist2 = [[inf] * N for _ in range(N)]
    for i in range(N):
        dist2[i][i] = 0
    for u, v in uv:
        dist2[u][v] = dist2[v][u] = dist[u][v]

    prev = [[i] * N for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist2[i][k] == inf or dist2[k][j] == inf: continue
                d = dist2[i][k] + dist2[k][j]
                if d >= dist2[i][j]: continue
                dist2[i][j] = d
                prev[i][j] = prev[k][j]


    edge_idx = []
    for i in range(M):
        u, v = uv[i]
        if dist2[u][v] < dist[u][v]: continue
        edge_idx.append(i)
    edge_idx = sorted(edge_idx, key=lambda i: dist[uv[i][0]][uv[i][1]])
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
