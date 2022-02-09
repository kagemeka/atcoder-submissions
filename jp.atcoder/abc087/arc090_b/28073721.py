import typing
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1
        g[l].append((r, d))
        g[r].append((l, -d))

    inf = 1 << 60
    x = [inf] * n
    def dfs(i: int) -> bool:
        for j, d in g[i]:
            if x[j] != inf:
                if x[i] + d != x[j]: return False
                continue
            x[j] = x[i] + d
            dfs(j)
        return True

    ok = True
    for i in range(n):
        if x[i] != inf: continue
        x[i] = 0
        ok &= dfs(i)
    print('Yes' if ok else 'No')

main()
