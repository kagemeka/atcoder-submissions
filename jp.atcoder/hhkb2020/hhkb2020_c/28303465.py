import typing


def main() -> typing.NoReturn:
    n = int(input())
    p = list(map(int, input().split()))
    k = 1 << 20

    appeared = [False] * k
    mn = 0
    for x in p:
        appeared[x] = True
        while appeared[mn]: mn += 1
        print(mn)

main()
