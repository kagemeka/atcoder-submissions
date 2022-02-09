import typing


def main() -> typing.NoReturn:
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))

    x = 0
    y = 0
    for i in range(n - 1):
        x += p[i] < p[i + 1]
        y += p[i] > p[i + 1]

    if y == 0:
        print(0)
        return
    if x == 0:
        print(1)
        return

    if y == 1:
        for i in range(n - 1):
            if p[i] > p[i + 1]: break

        print(min(i + 1, 2 + n - 1 - i))
        return

    if x == 1:
        for i in range(n - 1):
            if p[i] < p[i + 1]: break
        print(1 + min(i + 1, n - 1 - i))
        return

    raise

main()
