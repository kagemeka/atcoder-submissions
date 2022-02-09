import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pos = 0
    neg = 0
    for i in range(n):
        if a[i] > b[i]:
            neg += a[i] - b[i]
        else:
            pos += (b[i] - a[i]) // 2
    print('Yes' if pos >= neg else 'No')

main()
