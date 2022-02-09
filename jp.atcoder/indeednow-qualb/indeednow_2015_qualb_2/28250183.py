import typing


def main() -> typing.NoReturn:
    s = input()
    t = input()

    n = len(s)
    if len(t) != n:
        print(-1)
        return
    for i in range(n):
        w = s[-i:] + s[:-i]
        if w == t:
            print(i)
            return
    print(-1)

main()
