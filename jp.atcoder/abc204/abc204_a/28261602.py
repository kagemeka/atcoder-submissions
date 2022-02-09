import typing


def main() -> typing.NoReturn:
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(((x + 1) ^ (y + 1)) - 1)

main()
