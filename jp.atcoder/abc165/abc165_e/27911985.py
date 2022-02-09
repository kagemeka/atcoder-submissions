import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = range(m)[::-1]
    b = range(m, m + m)
    for x, y in zip(a, b):
        print(x + 1, y + 1)


main()
