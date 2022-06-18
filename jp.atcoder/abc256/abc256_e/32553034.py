# mypy: ignore-errors

import sys

sys.setrecursionlimit(10**6)


def main() -> None:
    # reverse smallest in each cycle

    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    b = list(map(int, input().split()))

    g = [[] for _ in range(n)]
    for i in range(n):
        g[a[i]].append((i, b[i]))
    on_stack = [False] * n
    visited = [False] * n

    s = 0

    def dfs(u: int, c: int) -> None:
        visited[u] = True
        on_stack[u] = True

        for v, nc in g[u]:
            nc = min(c, nc)
            if not visited[v]:
                dfs(v, nc)
            elif on_stack[v]:
                nonlocal s
                s += nc

        on_stack[u] = False

    inf = 1 << 60
    for i in range(n):
        if not visited[i]:
            dfs(i, inf)
    print(s)


if __name__ == "__main__":
    main()
