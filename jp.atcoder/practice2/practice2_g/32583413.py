# mypy: ignore-errors

import typing

G = typing.List[typing.List[int]]
L = typing.List[int]


def _t(g: G) -> G:
    n = len(g)
    g2: G = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            g2[v].append(u)
    return g2


def kosaraju(g: G) -> L:
    n = len(g)
    vis = [False] * n
    q = []

    def dfs(u: int) -> None:
        vis[u] = True
        for v in g[u]:
            if not vis[v]:
                dfs(v)
        q.append(u)

    for u in range(n):
        if not vis[u]:
            dfs(u)

    g = _t(g)
    label = [-1] * n

    def rdfs(u: int, l: int) -> None:
        label[u] = l
        for v in g[u]:
            if label[v] == -1:
                rdfs(v, l)

    l = 0
    for u in q[::-1]:
        if label[u] == -1:
            rdfs(u, l)
            l += 1
    return label


def main() -> None:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)

    labels = kosaraju(g)
    # assert all(l != -1 for l in labels)
    k = max(labels) + 1
    comp = [[] for _ in range(k)]
    print(k)
    for i in range(n):
        comp[labels[i]].append(i)
    for c in comp:
        print(len(c), *c)


import sys

sys.setrecursionlimit(1 << 20)

main()
