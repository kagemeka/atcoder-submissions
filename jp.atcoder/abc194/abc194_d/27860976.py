import typing


def main() -> typing.NoReturn:
    n = int(input())
    ex = 0
    for i in range(n - 1, 0, -1):
        ex += n / (n - i)
    print(ex)

main()
