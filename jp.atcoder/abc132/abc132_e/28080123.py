import typing



def main() -> typing.NoReturn:
    # dist[r][i] := shortest dist to i such that d % 3 == r
    # bfs
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)

    s, t = map(int, input().split())
    s -= 1
    t -= 1

    inf = 1 << 20
    dist = [[inf] * n for _ in range(3)]
    dist[0][s] = 0
    que = [(s, 0)]
    for u, ru in que:
        rv = (ru + 1) % 3
        dv = dist[ru][u] + 1
        for v in g[u]:
            if dv >= dist[rv][v]: continue
            dist[rv][v] = dv
            que.append((v, rv))
    d = dist[0][t]
    print(-1 if d == inf else d // 3)

main()
