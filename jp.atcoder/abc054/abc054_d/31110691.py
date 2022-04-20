def main() -> None:
    n, ma, mb = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(n)]

    K = 1 << 9
    INF = 1 << 60
    dp = [[INF] * K for _ in range(K)]
    dp[0][0] = 0
    for a, b, c in abc:
        for i in range(K - 1, a - 1, -1):
            for j in range(b, K):
                dp[i][j] = min(dp[i][j], dp[i - a][j - b] + c)

    min_cost = INF
    for i in range(1, K):
        if i * ma >= K or i * mb >= K:
            break
        min_cost = min(min_cost, dp[i * ma][i * mb])
    print(-1 if min_cost == INF else min_cost)


if __name__ == "__main__":
    main()
