import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    y, x = map(int, input().split())

    print(h * w - y * w - x * h + y * x)

main()
