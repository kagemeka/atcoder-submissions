def main() -> None:
    n, m, k = map(int, input().split())
    MOD = 998_244_353

    # dp
    K = 1 << 13
    dp = [0] * K
    dp[0] = 1
    for _ in range(n):
        ndp = [0] * K
        for i in range(1, m + 1):
            for j in range(i, K):
                ndp[j] += dp[j - i]
                ndp[j] %= MOD
        dp = ndp
    # print(dp)
    print(sum(dp[: k + 1]) % MOD)


if __name__ == "__main__":
    main()
