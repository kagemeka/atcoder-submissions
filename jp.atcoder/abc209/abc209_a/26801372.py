import typing


def main() -> typing.NoReturn:
    a, b = map(int, input().split())
    print(b - a + 1)


main()
