import typing


def main() -> typing.NoReturn:
    n = int(input())
    print(n * (n - 1) // 2)

main()
