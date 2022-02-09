import typing

def main() -> typing.NoReturn:
    x, y, z = map(int, input().split())
    print((z * y + x - 1) // x - 1)

main()
