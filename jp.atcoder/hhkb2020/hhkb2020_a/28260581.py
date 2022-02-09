import typing


def main() -> typing.NoReturn:
    s = input()
    t = input()
    print(t.upper() if s == 'Y' else t)

main()
