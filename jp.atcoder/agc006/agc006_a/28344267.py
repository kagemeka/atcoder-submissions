import typing


def main() -> typing.NoReturn:
    n = int(input())
    s = input()
    t = input()


    for i in range(n):
        if s[i:] != t[:n - i]: continue
        print(n + i)
        return

    print(2 * n)

main()
