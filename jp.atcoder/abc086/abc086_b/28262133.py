import typing


def main() -> typing.NoReturn:
    a, b = input().split()
    c = int(a + b)
    for x in range(1, 1000):
        if c == x * x:
            print('Yes')
            return
    print('No')

main()
