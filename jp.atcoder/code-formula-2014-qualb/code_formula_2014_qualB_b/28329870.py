import typing


def main() -> typing.NoReturn:
    s = input()
    s = s[::-1]
    x = y = 0
    for i, d in enumerate(s):
        d = int(d)
        if i & 1: y += d
        else: x += d

    print(y, x)

main()
