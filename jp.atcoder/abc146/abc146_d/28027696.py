import typing


def main() -> typing.NoReturn:
    n = int(input())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

    g = [[] for _ in range(n)]
    for i, (a, b) in enumerate(ab):
        g[a].append((b, i))
        g[b].append((a, i))

    color = [-1] * (n - 1)
    parent = [-1] * n
    def dfs(u: int, c0: int) -> typing.NoReturn:
        c = 0
        for v, i in g[u]:
            if v == parent[u]: continue
            if c == c0: c += 1
            color[i] = c + 1
            parent[v] = u
            dfs(v, c)
            c += 1
    dfs(0, -1)
    assert all(c != -1 for c in color)
    print(max(color))
    print(*color, sep='\n')

main()
