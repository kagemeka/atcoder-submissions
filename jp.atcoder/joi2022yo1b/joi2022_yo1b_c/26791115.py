import typing


def main() -> typing.NoReturn:
    n = int(input())
    s = input()
    for i in range(n - 1):
        if s[i + 1] == 'J': print(s[i])

main()
