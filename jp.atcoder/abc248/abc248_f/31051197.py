def main() -> None:
    n, p = map(int, input().split())

    # dp

    dp = [[0, 0] for _ in range(n)]

    dp[0][1] = 1
    dp[1][0] = 1
    for _ in range(n - 1):
        ndp = [[0, 0] for _ in range(n)]
        for i in range(n):
            ndp[i][1] += dp[i][1] + dp[i][0]
            if i >= 1:
                ndp[i][1] += dp[i - 1][1]
                ndp[i][0] += dp[i - 1][0]
                ndp[i][1] += dp[i - 1][1] * 2
            if i >= 2:
                ndp[i][0] += dp[i - 2][1] * 2
        for i in range(n):
            ndp[i][0] %= p
            ndp[i][1] %= p
        dp = ndp
    res = [dp[i][1] for i in range(1, n)]
    print(*res)


if __name__ == "__main__":
    main()
