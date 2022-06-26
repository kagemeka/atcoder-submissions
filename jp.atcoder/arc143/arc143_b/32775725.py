# / mypy: ignore-errors
import typing


# combinations

MOD = 998_244_353

K = 1 << 18
fact = list(range(K))
fact[0] = 1
for i in range(K - 1):
    fact[i + 1] = fact[i] * fact[i + 1] % MOD

ifact = list(range(1, K + 1))
ifact[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(K - 1, 0, -1):
    ifact[i - 1] = ifact[i - 1] * ifact[i] % MOD


def choose(n: int, k: int) -> int:
    if not 0 <= k <= n:
        return 0
    return fact[n] * ifact[k] % MOD * ifact[n - k] % MOD


def main() -> None:
    n = int(input())
    m = n * n

    p = 0
    for i in range(1, m + 1):
        p += choose(m - i, n - 1) * choose(i - 1, n - 1) % MOD
        p %= MOD
    p *= fact[n] * fact[n] % MOD * fact[n * n - 2 * n + 1] % MOD
    p %= MOD
    ans = fact[n * n] - p
    ans %= MOD
    print(ans)


main()
