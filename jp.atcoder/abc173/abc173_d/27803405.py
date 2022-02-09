import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    k = n - 2
    h = a[0]
    a = a[1:]
    h += 2 * sum(a[:k // 2])
    if k & 1:
        h += a[k // 2]
    print(h)

main()
