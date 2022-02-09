import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    s = (1 + n) * n // 2 * k * 100 + (1 + k) * k // 2 * n
    print(s)

main()
