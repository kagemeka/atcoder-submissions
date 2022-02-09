import typing


def main() -> typing.NoReturn:
    n = int(input())

    s = ''
    while n:
        if n & 1:
            s += 'A'
        s += 'B'
        n >>= 1
    print(s[::-1])

main()
