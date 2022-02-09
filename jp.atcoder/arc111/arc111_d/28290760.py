import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    # for edge (u, v), if c[u] < c[v], edge direction is <-,
    # and else if c[v] > c[v], it's ->.
    # if c[u] == c[v], u and v are parts of a cycle which size is more than 2.
    # dfs
    # (to, is_rev, edge_id)

    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append((b, 0, i))
        g[b].append((a, 1, i))

    res = [-1] * m
    c = list(map(int, input().split()))

    # dfs
    # use only edges such that c[u] > c[v] or, c[u] == c[v] \land the direction is not fixed.


    def dfs(u: int) -> typing.NoReturn:
        for v, dir_, edge_id in g[u]:
            if res[edge_id] != -1: continue # already fixed.
            if c[u] < c[v]: continue
            res[edge_id] = dir_
            dfs(v)

    for u in range(n):
        dfs(u)

    for d in res:
        print('<-' if d else '->')

main()
