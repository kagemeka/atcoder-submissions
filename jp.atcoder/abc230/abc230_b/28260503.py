import typing


def main() -> typing.NoReturn:
    s = input()
    t = 'oxx' * 10 ** 5
    print('Yes' if s in t else 'No')


main()
