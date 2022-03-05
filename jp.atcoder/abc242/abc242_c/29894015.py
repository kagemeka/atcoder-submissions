def main() -> None:
    n = int(input())
    MOD = 998_244_353

    dp = [[0] * 9 for _ in range(n)]
    for j in range(9):
        dp[0][j] = 1
    for i in range(n - 1):
        for j in range(9):
            if j < 8:
                dp[i + 1][j] += dp[i][j + 1]
            if j > 0:
                dp[i + 1][j] += dp[i][j - 1]
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    print(sum(dp[-1]) % MOD)


if __name__ == "__main__":
    main()
