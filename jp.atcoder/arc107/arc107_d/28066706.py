import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    MOD = 998_244_353
    dp = [[0] * (2 * n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][j * 2]) % MOD

    print(dp[n][k])

main()
