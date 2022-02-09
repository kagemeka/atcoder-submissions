import typing


def main() -> typing.NoReturn:
    a, b, c, d = map(int, input().split())
    mx = max(a * c, a * d, b * c, b * d)
    print(mx)

main()
