import typing


def floyd_warshall(
    g: typing.List[typing.List[int]],
) -> typing.List[typing.List[int]]:
    import copy
    g = copy.deepcopy(g)
    inf = 1 << 60
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][k] == inf or g[k][j] == inf: continue
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g


def main() -> typing.NoReturn:
    n, m, l = map(int, input().split())
    inf = 1 << 60
    g = [[inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a][b] = g[b][a] = c

    for i in range(n):
        g[i][i] = 0
    g = floyd_warshall(g)
    for i in range(n):
        for j in range(n):
            if 1 <= g[i][j] <= l: g[i][j] = 1
            elif l < g[i][j]: g[i][j] = inf
    g = floyd_warshall(g)
    q = int(input())
    st = [tuple(map(int, input().split())) for _ in range(q)]
    for s, t in st:
        s -= 1
        t -= 1
        cnt = g[s][t]
        print(-1 if cnt == inf else cnt - 1)

main()
