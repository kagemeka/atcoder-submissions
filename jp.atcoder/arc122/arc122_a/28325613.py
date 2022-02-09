import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    # DP
    MOD = 10 ** 9 + 7

    k = 1 << 18
    fib = [0] * k
    fib[1] = 1
    for i in range(2, k):
        fib[i] = (fib[i - 2] + fib[i - 1]) % MOD

    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = sum(dp[i]) + fib[i + 1] * a[i]
        dp[i + 1][1] = dp[i][0] - fib[i] * a[i]
        dp[i + 1][0] %= MOD
        dp[i + 1][1] %= MOD

    print(sum(dp[-1]) % MOD)

main()
