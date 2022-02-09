import typing


def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    # dp

    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = x
    mn = x
    for i in range(n - 1):
        p = a[i + 1] // a[i]
        dp[i + 1], dp[i] = divmod(dp[i], p)
        assert p > dp[i]
        if p - dp[i] + 1 <= dp[i]:
            dp[i + 1] += 1
            dp[i] = p - dp[i]
        mn = min(mn, sum(dp))
    print(mn)

main()
