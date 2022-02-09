import typing


def main() -> typing.NoReturn:
    a, b = map(int, input().split())
    if a < b: a, b = b, a

    print(a * 2 - (a != b))

main()
