def main() -> None:
    # consider putting (a, b) pairs as nodes.
    # O(N^2 + M^2)

    INF = 1 << 60
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = input().split()
        a = int(a) - 1
        b = int(b) - 1
        c = ord(c) - 97
        g[a].append((b, c))
        g[b].append((a, c))

    # on_stack = [[False] * n for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dist[0][n - 1] = 0
    que = [(0, n - 1)]
    for u, v in que:
        for nu, s in g[u]:
            for nv, t in g[v]:
                if s != t:
                    continue
                next_dist = dist[u][v] + 1
                if next_dist >= dist[nu][nv]:
                    continue
                dist[nu][nv] = next_dist
                que.append((nu, nv))

    min_dist = INF
    for i in range(n):
        min_dist = min(min_dist, dist[i][i] * 2)
    for i in range(n):
        for j, _ in g[i]:
            min_dist = min(min_dist, 1 + dist[i][j] * 2)
    print(-1 if min_dist == INF else min_dist)


if __name__ == "__main__":
    main()
