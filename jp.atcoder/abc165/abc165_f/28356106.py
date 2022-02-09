import typing
import bisect
import sys

sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)


    # DFS
    # share LIS array globally for memory saving.
    # memorize how the LIS was changed at each node.
    # undo the operation conducted on the node at returning point of DFS function.

    inf = 1 << 60
    lis = [inf] * n
    res = [-1] * n
    def dfs(u: int, p: int) -> None:
        i = bisect.bisect_left(lis, a[u])
        x = lis[i]
        lis[i] = a[u]
        res[u] = bisect.bisect_left(lis, inf)
        for v in g[u]:
            if v == p: continue
            dfs(v, u)
        lis[i] = x

    dfs(0, -1)
    print(*res, sep='\n')

main()
