import typing


def main() -> typing.NoReturn:
    s = input()
    a, b = map(int, s.split('x'))
    print(a * b)

main()
