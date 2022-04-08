def main() -> None:
    n, s = map(int, input().split())

    a = list(map(int, input().split()))
    K = 1 << 12
    dp = [0] * K

    MOD = 998_244_353
    dp[0] = 1
    for x in a:
        ndp = [0] * K
        for i in range(K):
            ndp[i] += dp[i] * 2  # not in t, or not in S
            if i >= x:
                ndp[i] += dp[i - x]  # in S
            ndp[i] %= MOD
        dp = ndp
    print(dp[s])


if __name__ == "__main__":
    main()
