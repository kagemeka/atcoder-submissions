import typing


def main() -> typing.NoReturn:
    x, y = map(int, input().split())
    s = 0
    s += max(4 - x, 0) * 10 ** 5
    s += max(4 - y, 0) * 10 ** 5
    if x == y == 1:
        s += 4 * 10 ** 5
    print(s)

main()
