import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    s = sum(abs(a[i + 1] - a[i]) for i in range(n + 1))
    for i in range(1, n + 1):
        d0 = a[i] - a[i - 1]
        d1 = a[i + 1] - a[i]
        if d0 * d1 >= 0:
            print(s)
            continue
        print(s - abs(d0) - abs(d1) + abs(a[i + 1] - a[i - 1]))

main()
