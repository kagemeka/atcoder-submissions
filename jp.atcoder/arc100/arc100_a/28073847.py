import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    b = a[n // 2] if n & 1 else (a[n // 2] + a[n // 2 - 1]) // 2
    s = sum(abs(x - b) for x in a)
    print(s)

main()
