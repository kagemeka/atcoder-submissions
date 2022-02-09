import typing


def main() -> typing.NoReturn:
    n = int(input())

    s = 0
    for i in range(1, n + 1):
        j = n // i
        s += (1 + j) * i * j // 2
    print(s)

main()
