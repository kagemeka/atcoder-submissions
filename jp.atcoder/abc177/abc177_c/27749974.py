import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 1_000_000_007
    s = sum(a) % MOD
    s2 = 0
    for x in a:
        s2 += x * x
    s2 %= MOD
    print((s * s % MOD - s2) * pow(2, -1, MOD) % MOD)

main()
