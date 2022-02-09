import typing

def main() -> typing.NoReturn:
    n, s = map(int, input().split())
    k = 1 << 12
    a = list(map(int, input().split()))

    dp = [0] * k
    dp[0] = 1
    MOD = 998_244_353
    for x in a:
        for i in range(k - 1, -1, -1):
            dp[i] *= 2
            if i - x >= 0: dp[i] += dp[i - x]
            dp[i] %= MOD
    print(dp[s])

main()
