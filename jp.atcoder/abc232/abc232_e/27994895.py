import typing  


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())
    x0, y0, x1, y1 = map(int, input().split())
    MOD = 998_244_353
    dp = [[0] * (1 << 2) for _ in range(k + 1)]
    i = 0
    if x0 == x1:
        i |= 1 << 0
    if y0 == y1:
        i |= 1 << 1
    dp[0][i] = 1

    for i in range(k):
        dp[i + 1][0] = dp[i][0] * (h + w - 4) + dp[i][1] * (h - 1) + dp[i][2] * (w - 1)
        dp[i + 1][1] = dp[i][0] + dp[i][1] * (w - 2) + dp[i][3] * (w - 1)
        dp[i + 1][2] = dp[i][0] + dp[i][2] * (h - 2) + dp[i][3] * (h - 1)
        dp[i + 1][3] = dp[i][1] + dp[i][2]
        for j in range(4):
            dp[i + 1][j] %= MOD
    print(dp[-1][3])

main()