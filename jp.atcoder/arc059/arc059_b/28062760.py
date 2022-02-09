import typing


def main() -> typing.NoReturn:
    s = input()
    n = len(s)
    for i in range(n - 1):
        if s[i] != s[i + 1]: continue
        print(i + 1, i + 2)
        return
    for i in range(n - 2):
        if s[i] != s[i + 2]: continue
        print(i + 1, i + 3)
        return
    print(-1, -1)

main()
