def main() -> None:
    n, m = map(int, input().split())

    # the distance of the two vertices is not changed after floyd warshall,
    # if possibly contained.

    inf = 1 << 60
    edges = []
    dist = [[inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = dist[b][a] = c
        edges.append((a, b, c))

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print(sum(dist[a][b] < c for a, b, c in edges))


if __name__ == "__main__":
    main()
