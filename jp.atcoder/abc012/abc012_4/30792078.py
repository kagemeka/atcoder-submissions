def main() -> None:
    n, m = map(int, input().split())

    inf = 1 << 60

    dist = [[inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = dist[b][a] = t

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    d = min(max(dist[i]) for i in range(n))
    print(d)


if __name__ == "__main__":
    main()
