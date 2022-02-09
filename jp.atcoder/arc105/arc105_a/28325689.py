import typing


def main() -> typing.NoReturn:
    a = list(map(int, input().split()))
    a.sort()
    print('Yes' if a[0] + a[3] == a[1] + a[2] else 'No')

main()
