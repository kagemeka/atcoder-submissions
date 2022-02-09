import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = []
    b = []
    for d in range(1, m + 1):
        if d & 1:
            x = (m + 1) // 2
            a.append(x - d // 2)
            b.append(x + (d + 1) // 2)
        else:
            x = n - m // 2
            a.append(x + d // 2)
            b.append(x - d // 2)

    for x, y in zip(a, b):
        print(x, y)


main()
