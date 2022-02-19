import typing


def main() -> typing.NoReturn:
    n = int(input())
    print((n + 1000 - 1) // 1000 * 1000 - n)

main()
