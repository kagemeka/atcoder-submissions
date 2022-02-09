import typing


def main() -> typing.NoReturn:
    n = map(int, input())
    print('Yes' if sum(n) % 9 == 0 else 'No')

main()
