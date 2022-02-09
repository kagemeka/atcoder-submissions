import typing


def main() -> typing.NoReturn:
    # similar to LCS (Longest Common Subsequence)
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]
            if s[i] != t[j]:
                dp[i + 1][j + 1] -= dp[i][j]
            dp[i + 1][j + 1] %= MOD
    print(dp[-1][-1])

main()
