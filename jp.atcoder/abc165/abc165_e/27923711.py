import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    # a = [-1] * m
    # b = [-1] * m
    # a[::2] = range((m + 1) // 2)
    # b[:] = range((m + 1) // 2, (m + 1) // 2 + m)
    # a[1::2] = range((m + 1) // 2 + m, m + m)
    # b[:] = range(m, m + m)
    a = range(m)[::-1]
    b = range(n - m, n)
    for x, y in zip(a, b):
        print(x + 1, y + 1)


main()
