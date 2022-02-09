import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    # let g := GCD(A)
    # for each g, count up the number of A such that GCD(A) = g
    # let this function as f(g)
    # f(d) = (K // d)^N - \sum_{g=d * 2, step=d}^{K}f(g)

    MOD = 10 ** 9 + 7

    cnt = [0] * (k + 1)
    for d in range(k, 0, -1):
        cnt[d] = pow(k // d, n, MOD)
        for g in range(d * 2, k + 1, d):
            cnt[d] -= cnt[g]
        cnt[d] %= MOD

    s = 0
    for d in range(1, k + 1):
        s += d * cnt[d] % MOD
    s %= MOD
    print(s)

main()
