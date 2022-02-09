import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = range(1, m + 1)
    b = range(n, n - m, - 1)
    for x, y in zip(a, b):
        print(x, y)


main()
