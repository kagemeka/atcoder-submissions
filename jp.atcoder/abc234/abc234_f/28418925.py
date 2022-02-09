
def main() -> None:
    s = input()
    MOD = 998_244_353


    n = len(s)
    k = 1 << 13
    fact = list(range(k))
    fact[0] = 1
    for i in range(k - 1):
        fact[i + 1] = fact[i] * fact[i + 1] % MOD
    ifact = [pow(fact[i], MOD - 2, MOD) for i in range(k)]
    choose = lambda n, k: fact[n] * ifact[n - k] % MOD * ifact[k] % MOD

    dp = [0] * (n + 1)
    dp[0] = 1
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - 97] += 1
    cnt.sort()
    for c in cnt:
        for i in range(n, 0, -1):
            if dp[i - c] == 0: continue
            for j in range(1, c + 1):
                if i - j < 0: break
                dp[i] += dp[i - j] * choose(i, j) % MOD
                dp[i] %= MOD

    print((sum(dp) - 1) % MOD)




main()
