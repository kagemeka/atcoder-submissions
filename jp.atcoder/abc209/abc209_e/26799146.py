import typing
import sys
import string
import functools
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n = int(input())
    s = sys.stdin.read().split()
    alp = string.ascii_letters
    m = len(alp)
    to_int = dict(zip(alp, range(m)))

    head = [-1] * n
    tail = [-1] * n
    for i in range(n):
        w = s[i]
        v = 0
        d = 1
        for c in w[:3][::-1]:
            v += to_int[c] * d
            d *= m
        head[i] = v
        v = 0
        d = 1
        for c in w[-3:][::-1]:
            v += to_int[c] * d
            d *= m
        tail[i] = v
    g = [[] for _ in range(1 << 18)]
    for i in range(n):
        g[head[i]].append(i)

    visited = [False] * n
    @functools.lru_cache(maxsize=None)
    def dfs(u: int) -> int:
        if not g[tail[u]]: return 0
        if visited[u]: return 1
        visited[u] = True
        res = 0
        for v in g[tail[u]]:
            res = max(res, dfs(v))
        return 2 - res

    for i in range(n):
        res = dfs(i)
        print('Takahashi' if res == 0 else 'Draw' if res == 1 else 'Aoki')


main()
