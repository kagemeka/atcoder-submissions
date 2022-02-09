import typing

def main() -> typing.NoReturn:
    h, a = map(int, input().split())
    print((h + a - 1) // a)

main()
