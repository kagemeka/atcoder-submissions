import typing


def main() -> None:
    n, m, k = map(int, input().split())
    mod = 998_244_353

    # cumulative sum
    # imos algorithm

    dp = [1] * m
    for _ in range(n - 1):
        ndp = [0] * m
        for i in range(m):
            j = i - k
            if j >= 0:
                ndp[0] += dp[i]
                ndp[j + 1] -= dp[i]
            j = i + k
            if j < m:
                ndp[j] += dp[i]
        ndp[0] %= mod
        for i in range(m - 1):
            ndp[i + 1] += ndp[i]
            ndp[i + 1] %= mod
        dp = ndp
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
