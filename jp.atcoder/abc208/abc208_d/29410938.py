def main() -> None:
    n, m = map(int, input().split())
    # progress of floyd warshall

    INF = 1 << 60
    dist = [[INF] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = c

    for i in range(n):
        dist[i][i] = 0

    dist_sum = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                dist_sum += dist[i][j] if dist[i][j] < INF else 0
    print(dist_sum)


main()
