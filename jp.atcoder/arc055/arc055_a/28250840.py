import typing


def main() -> typing.NoReturn:
    n = int(input())
    print('1' + '0' * (n - 1) + '7')

main()
