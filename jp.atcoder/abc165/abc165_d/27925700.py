import typing


def main() -> typing.NoReturn:
    a, b, n = map(int, input().split())
    x = b - 1 if n >= b - 1 else n
    print(a * x // b)

main()
