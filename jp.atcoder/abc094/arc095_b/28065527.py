import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()


    y = a[n - 1]
    x = -1
    mx = 0
    for j in range(n - 1):
        d = min(a[j], y - a[j])
        if d < mx: continue
        x = a[j]
        mx = d
    print(y, x)


main()
