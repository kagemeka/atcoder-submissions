import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    s = n * sum(x ** 2 for x in a) - sum(a) ** 2
    print(s)

main()
