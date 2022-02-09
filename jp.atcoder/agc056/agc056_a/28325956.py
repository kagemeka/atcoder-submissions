import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(i * 3, (i + 1) * 3):
            j %= n
            a[i][j] = '#'

    if n % 3:
        a[0], a[n // 3] = a[n // 3], a[0]
        a[n - 1], a[n - 1 - n // 3] = a[n - 1 - n // 3], a[n - 1]
    for s in a:
        print(''.join(s))

main()
