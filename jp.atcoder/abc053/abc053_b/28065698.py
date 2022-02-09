import typing


def main() -> typing.NoReturn:
    s = input()
    i = s.index('A')
    j = len(s) - s[::-1].index('Z')
    print(j - i)

main()
