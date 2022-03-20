def main() -> None:
    n, m, k, s, t, x = map(int, input().split())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    for u, v in uv:
        g[u].append(v)
        g[v].append(u)

    s -= 1
    t -= 1
    x -= 1
    dp = [[0] * 2 for _ in range(n)]
    dp[s][0] = 1
    MOD = 998_244_353

    for _ in range(k):
        ndp = [[0] * 2 for _ in range(n)]
        for u in range(n):
            for v in g[u]:
                if v == x:
                    ndp[v][0] += dp[u][1]
                    ndp[v][1] += dp[u][0]
                else:
                    ndp[v][0] += dp[u][0]
                    ndp[v][1] += dp[u][1]
        for u in range(n):
            for j in range(2):
                ndp[u][j] %= MOD
        dp = ndp
    print(dp[t][0] % MOD)


if __name__ == "__main__":
    main()
