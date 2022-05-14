def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    inf = 1 << 60

    res = inf
    dp = [[inf] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = inf

    for i in range(1, n):
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

    res = min(res, dp[-1][1])
    dp = [[inf] * 2 for _ in range(n)]
    # dp[0][0] = 0
    dp[0][1] = a[0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

    res = min(res, min(dp[-1]))
    print(res)


if __name__ == "__main__":
    main()
