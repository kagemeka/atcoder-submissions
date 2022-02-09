import typing


def main() -> typing.NoReturn:
    n, k, m = map(int, input().split())
    MOD = 998_244_353
    # res = pow(m, pow(k, n, MOD - 1), MOD)
    res = pow(m, pow(k, n), MOD)
    print(res)


main()
