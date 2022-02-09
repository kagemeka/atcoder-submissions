import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ok = [True] * n
    for i in range(n - 1):
        ok[i] = a[i + 1] <= a[i] * 2
        a[i + 1] += a[i]
    for i in range(n - 1, 0, -1):
        ok[i - 1] &= ok[i]

    print(sum(ok))

main()
