import typing




def main() -> typing.NoReturn:
    a, b = input().split('.')
    print(int(a) + (int(b[0]) >= 5))


main()
