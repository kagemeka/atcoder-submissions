import typing


def bfs_sparse(
    g: typing.List[typing.List[int]],
    src: int,
) -> typing.List[int]:
    inf = 1 << 60
    n = len(g)
    dist = [inf] * n
    dist[src] = 0
    que = [src]
    for u in que:
        for v in g[u]:
            dv = dist[u] + 1
            if dv >= dist[v]: continue
            dist[v] = dv
            que.append(v)
    return dist


def main() -> typing.NoReturn:
    # pre-compute distance for all c_i, c_j (0 <= i, j < k).
    # TSP
    # O(K(N + M) + K^22^K) # bfs * K + TSP

    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    k = int(input())
    c = list(map(lambda x: int(x) - 1, input().split()))

    inf = 1 << 60
    dist = [[inf] * k for _ in range(k)]
    for i in range(k):
        d = bfs_sparse(g, c[i])
        for j in range(k):
            dist[i][j] = d[c[j]]


    dp = [[inf] * k for _ in range(1 << k)]
    for i in range(k):
        dp[1 << i][i] = 1
    for s in range(1 << k):
        for i in range(k):
            if ~s >> i & 1: continue
            t = s & ~(1 << i)
            for j in range(k):
                if ~t >> j & 1: continue
                dp[s][i] = min(dp[s][i], dp[t][j] + dist[j][i])

    mn = min(dp[-1])
    print(-1 if mn == inf else mn)


main()
