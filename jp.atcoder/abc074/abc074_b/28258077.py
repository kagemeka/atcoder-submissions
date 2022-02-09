import typing


def main() -> typing.NoReturn:
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))

    s = 0
    for x in a:
        s += 2 * min(x, k - x)
    print(s)

main()
