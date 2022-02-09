import typing


def main() -> typing.NoReturn:
    x, y = map(int, input().split())
    if x > y: x, y = y, x
    print('Yes' if x + 3 > y else 'No')

main()
