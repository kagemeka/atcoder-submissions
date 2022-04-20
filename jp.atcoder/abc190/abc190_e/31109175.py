import sys
import typing

INF = 1 << 60


def shortest_path_bfs(
    graph: typing.List[typing.List[int]],
    src: int,
) -> typing.List[int]:
    n = len(graph)
    dist = [INF] * n
    dist[src] = 0
    que = [src]
    for u in que:
        for v in graph[u]:
            dv = dist[u] + 1
            if dv >= dist[v]:
                continue
            dist[v] = dv
            que.append(v)
    return dist


def traveling_salesperson(
    dist_matrix: typing.Sequence[typing.Sequence[int]],
    src: int,
) -> int:
    n = len(dist_matrix)
    assert all(len(row) == n for row in dist_matrix)

    dp = [[INF] * n for _ in range(1 << n)]
    dp[0][src] = 0
    for i in range(n):
        if i == src:
            continue
        dp[1 << i][i] = dist_matrix[src][i]

    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            for j in range(n):
                if ~t >> j & 1:
                    continue
                dp[s][i] = min(dp[s][i], dp[t][j] + dist_matrix[j][i])

    return dp[-1][src]


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    ab = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    k = int(sys.stdin.readline().rstrip())
    c = [int(x) for x in sys.stdin.readline().split()]

    g = [[] for _ in range(n)]
    for a, b in ab:
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    dist_matrix = [[INF] * (k + 1) for _ in range(k + 1)]
    for i in range(k):
        dist = shortest_path_bfs(g, c[i] - 1)
        for j in range(k):
            dist_matrix[i + 1][j + 1] = dist[c[j] - 1]
    for i in range(k):
        dist_matrix[i + 1][0] = dist_matrix[0][i + 1] = 0
    dist_matrix[0][0] = 0
    # tsp
    min_dist = traveling_salesperson(dist_matrix, 0)
    print(-1 if min_dist == INF else 1 + min_dist)


if __name__ == "__main__":
    main()
