import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    order = sorted(range(n), key=lambda i: a[i])
    print(*[i + 1 for i in order])

main()
