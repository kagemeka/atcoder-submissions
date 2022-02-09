import typing


def main() -> typing.NoReturn:
    # compute dist from a root.
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))


    inf = 1 << 60
    dist = [-1] * n
    dist[0] = 0
    parent = [-1] * n
    que = [0]
    for u in que:
        for v, w in g[u]:
            if v == parent[u]: continue
            dist[v] = dist[u] + w
            parent[v] = u
            que.append(v)

    for i in range(n):
        print(dist[i] & 1)


main()
