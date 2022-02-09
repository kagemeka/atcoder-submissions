import typing


def main() -> typing.NoReturn:
    d, t, s = map(int, input().split())
    print('Yes' if d <= s * t else 'No')

main()
