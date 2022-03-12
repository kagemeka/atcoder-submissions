def main() -> None:
    # floyd warshall
    n, m = map(int, input().split())
    inf = 1 << 60
    dist = [[inf] * n for _ in range(n)]
    use = [[False] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = dist[b][a] = c
        use[a][b] = use[b][a] = True

    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d = dist[i][k] + dist[k][j]
                if d > dist[i][j]:
                    continue
                dist[i][j] = d
                if k != i and k != j:
                    dist[i][j] = d
                    use[i][j] = False

    # print(use)
    # print(dist)
    needed = 0
    for i in range(n):
        for j in range(n):
            if not use[i][j]:
                use[j][i] = False
            if not use[j][i]:
                use[i][j] = False
            needed += use[i][j]
    # print(needed)
    needed //= 2

    print(m - needed)


if __name__ == "__main__":
    main()
