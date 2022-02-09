import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    p = 1 + 3 * (n - 1) + 6 * (k - 1) * (n - k)
    print(p / n ** 3)

main()
