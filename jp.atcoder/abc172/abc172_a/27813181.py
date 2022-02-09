import typing


def main() -> typing.NoReturn:
    a = int(input())
    print(a * (a * (a + 1) + 1))

main()
