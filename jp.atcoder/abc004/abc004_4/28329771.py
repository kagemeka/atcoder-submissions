import typing


def main() -> typing.NoReturn:
    r, g, b = map(int, input().split())

    # DP
    # place the center of red at 400, blue at 500, green at 600
    # 0 < x < 1024 (enough)
    k = 1 << 10


    inf = 1 << 60
    dp = [inf] * k
    dp[0] = 0

    for i in range(k - 1):
        ndp = [0] * k
        for j in range(1, k):
            x = 400 if j <= r else 500 if j <= r + g else 600
            ndp[j] = min(dp[j], dp[j - 1] + abs(i + 1 - x))

        dp = ndp

    print(dp[r + g + b])

main()
