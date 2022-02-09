import typing

def main() -> typing.NoReturn:
    s = input()
    t = input()
    n = len(s)
    print(sum(s[i] != t[i] for i in range(n)))

main()
