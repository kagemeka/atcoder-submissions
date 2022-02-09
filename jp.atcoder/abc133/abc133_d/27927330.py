import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if i & 1:
            s -= a[i]
        else:
            s += a[i]
    x = [-1] * n
    x[0] = s // 2
    for i in range(n - 1, 0, -1):
        x[i] = a[i] - x[(i + 1) % n]
    x = [y * 2 for y in x]
    print(*x)


main()
