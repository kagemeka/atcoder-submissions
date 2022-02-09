import typing

def main() -> typing.NoReturn:
    s = input()
    print(2 * min(s.count('0'), s.count('1')))

main()
