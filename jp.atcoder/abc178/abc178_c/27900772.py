import typing


def main() -> typing.NoReturn:
    n = int(input())
    MOD = 10 ** 9 + 7
    res = pow(10, n, MOD) - 2 * pow(9, n, MOD) + pow(8, n, MOD)
    print(res % MOD)

main()
