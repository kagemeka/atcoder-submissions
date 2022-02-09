import typing


def main() -> typing.NoReturn:
    x, y, z = map(int, input().split())
    n = (x - z) // (y + z)
    print(n)

main()
