import typing


def main() -> typing.NoReturn:
    a, b = input().split()
    c = int(a + b)
    for x in range(1, 102):
        if c == x * x:
            print('Yes')
            return
    print('No')

main()
