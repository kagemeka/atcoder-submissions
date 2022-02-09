import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a = [abs(x) for x in a]

    print(sum(a))
    print(sum(x ** 2 for x in a) ** .5)
    print(max(a))

main()
