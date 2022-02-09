import typing



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in xy:
        g[x].append(y)
        in_deg[y] += 1

    que = [i for i in range(n) if in_deg[i] == 0]
    inf = 1 << 60
    value = [0] * n
    min_h = [inf] * n
    for u in que:
        value[u] = a[u] - min_h[u]
        for v in g[u]:
            min_h[v] = min(min_h[v], min_h[u], a[u])
            in_deg[v] -= 1
            if in_deg[v] == 0: que.append(v)
    print(max(value))


main()
