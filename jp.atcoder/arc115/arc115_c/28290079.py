import typing


def main() -> typing.NoReturn:
    n = int(input())

    a = [1] * (n + 1)
    for i in range(1, n):
        for j in range(i * 2, n + 1, i):
            a[j] = max(a[j], a[i] + 1)

    print(*a[1:])

main()
