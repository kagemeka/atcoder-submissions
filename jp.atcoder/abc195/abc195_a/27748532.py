import typing


def main() -> typing.NoReturn:
    m, h = map(int, input().split())
    print('Yes' if h % m == 0 else 'No')


main()
