# from __future__ import annotations
import sys

sys.setrecursionlimit(1 << 22)
import typing


def main() -> None:
    n = int(input())

    # dfs
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    # root = 0
    inf = 1 << 30
    res = [(0, 0)] * n
    # mn = [inf] * n
    # mx = [-inf] * n
    label = 1



    def dfs(u: int, parent: int) -> typing.Tuple[int, int]:
        mx = -inf
        mn = inf
        for v in g[u]:
            if v == parent:
                continue
            l, r = dfs(v, u)
            if l < mn:
                mn = l
            if r > mx:
                mx = r
            # mn[u] = min(mn[u], mn[v])
            # mx[u] = max(mx[u], mx[v])
            # if mn[u] is None or mn[v] < mn[u]:
            #     mn[u] = mn[v]
            # if mx[u] is None or mx[v] > mx[u]:
            #     mx[u] = mx[v]
        nonlocal label
        if mn == inf:
            mn = mx = label
            label += 1
        res[u] = (mn, mx)
        return mn, mx

        # if mn[u] == inf:
        #     mn[u] = mx[u] = label
        #     label += 1

    dfs(0, -1)
    for l, r in res:
        print(l, r)
    # for l, r in zip(mn, mx):
    #     print(l, r)


if __name__ == "__main__":
    main()
