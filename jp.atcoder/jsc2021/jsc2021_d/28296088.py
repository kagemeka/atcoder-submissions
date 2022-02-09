import typing


def main() -> typing.NoReturn:
    n, p = map(int, input().split())
    MOD = 10 ** 9 + 7

    # for i >= 2, there is only one value that make \sum_{j=0}^{i} \equiv 0 \mod p
    # answer is (p - 1) * (p - 2) ^ (n - 1)


    print((p - 1) * pow(p - 2, n - 1, MOD) % MOD)


main()
