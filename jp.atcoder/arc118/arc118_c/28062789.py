import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = [1] * n
    for i in range(n - 1):
        a[i] *= 2
    for i in range(1, n):
        a[i] *= 3
    a[0] *= 5
    a[-1] *= 5
    print(*a)

main()
