import typing


def main() -> typing.NoReturn:
    a, b = map(int, input().split())

    if a + b == 15:
        print('+')
    elif a * b == 15:
        print('*')
    else:
        print('x')

main()
