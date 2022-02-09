import typing

def main() -> typing.NoReturn:
    s = input()
    s = sorted(s)
    print('Yes' if s[0] == s[1] and s[1] != s[2] and s[2] == s[3] else 'No')

main()
