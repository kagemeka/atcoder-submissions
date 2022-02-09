import typing


def main() -> typing.NoReturn:
    a, b, c, d, e = map(int, input().split())
    print(max(b + c + e, a + d + e))

main()
