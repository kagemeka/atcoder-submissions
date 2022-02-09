import typing


def main() -> typing.NoReturn:
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    m = n // 2
    print(d[m] - d[m - 1])

main()
