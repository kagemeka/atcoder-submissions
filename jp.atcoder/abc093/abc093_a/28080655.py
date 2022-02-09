import typing


def main() -> typing.NoReturn:
    s = input()
    s = ''.join(sorted(s))
    print('Yes' if s == 'abc' else 'No')

main()
