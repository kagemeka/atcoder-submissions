def main() -> None:
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    MOD = 10**9 + 7

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        dp[i + 1][0] = 1
    for j in range(m):
        dp[0][j + 1] = 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]
            if s[i] != t[j]:
                dp[i + 1][j + 1] -= dp[i][j]
            dp[i + 1][j + 1] %= MOD
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
