import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    if n > m: n, m = m, n

    if m == 1:
        print(1)
    elif n == 1:
        print(m - 2)
    else:
        print((n - 2) * (m - 2))

main()
