import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0
    for l in range(n):
        mn = 1 << 60
        for r in range(l, n):
            mn = min(mn, a[r])
            mx = max(mx, (r - l + 1) * mn)
    print(mx)

main()
