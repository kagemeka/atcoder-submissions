import typing


def main() -> typing.NoReturn:
    t = input()
    k = 13
    MOD = 10 ** 9 + 7
    dp = [0] * k
    dp[0] = 1
    for d in t:
        ndp = [0] * k
        for i in range(k):
            ndp[i * 10 % k] += dp[i]
        dp = ndp
        ndp = [0] * k
        if d != '?':
            d = int(d)
            for i in range(k):
                ndp[i] = dp[(i - d) % k]
        else:
            s = dp * 2
            for i in range(2 * k - 1):
                s[i + 1] += s[i]
                s[i + 1] %= MOD
            for i in range(k):
                ndp[i] = (s[k + i] - s[k + i - 10]) % MOD

        dp = ndp
    print(dp[5])

main()
