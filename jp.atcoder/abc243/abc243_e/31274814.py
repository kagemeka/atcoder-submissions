def main() -> None:
    n, m = map(int, input().split())
    INF = 1 << 60
    dist = [[INF] * n for _ in range(n)]
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b))
        dist[a][b] = dist[b][a] = c

    for i in range(n):
        dist[i][i] = 0

    needless = [[False] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d = dist[i][k] + dist[k][j]
                if d > dist[i][j]:
                    continue
                if k != i and k != j:
                    needless[i][j] = needless[j][i] = True
                dist[i][j] = d
    print(sum(needless[i][j] for i, j in edges))


if __name__ == "__main__":
    main()
