import typing


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())
    x0, y0, x1, y1 = map(int, input().split())

    MOD = 998_244_353
    dp = [0] * 4
    i = 0
    if x0 == x1:
        i |= 1 << 0
    if y0 == y1:
        i |= 1 << 1
    dp[i] = 1

    for _ in range(k):
        ndp = [0] * 4
        ndp[0] = dp[0] * (h + w - 4) + dp[1] * (h - 1) + dp[2] * (w - 1)
        ndp[1] = dp[0] + dp[1] * (w - 2) + dp[3] * (w - 1)
        ndp[2] = dp[0] + dp[2] * (h - 2) + dp[3] * (h - 1)
        ndp[3] = dp[1] + dp[2]
        for j in range(4):
            dp[j] = ndp[j] % MOD
    print(dp[-1])

main()
