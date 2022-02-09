import typing


def main() -> typing.NoReturn:
    a, b, c, d = map(int, input().split())

    l = (a + d - 1) // d
    r = (c + b - 1) // b
    print('Yes' if r <= l else 'No')


main()
